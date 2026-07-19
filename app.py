"""
NeuroMarket AI — MVP Dashboard
Sprint 2 kapsamında geliştirilmiş ilk çalışan ürün versiyonu.

Çalıştırmak için:
    pip install -r requirements.txt
    streamlit run app.py
"""

import re
from collections import Counter

import pandas as pd
import streamlit as st

st.set_page_config(page_title="NeuroMarket AI", page_icon="📊", layout="wide")

# ---------------------------------------------------------------------------
# 1) Duygu analizi — Türkçe anahtar kelime tabanlı basit kural motoru
#    (TextBlob gibi İngilizce odaklı kütüphaneler Türkçe metinlerde çalışmadığı
#    için Sprint 2 MVP kapsamında bu yaklaşım tercih edilmiştir. Sprint 3'te
#    Türkçe destekli bir transformer modeliyle değiştirilecektir.)
# ---------------------------------------------------------------------------
POSITIVE_WORDS = [
    "harika", "güzel", "memnun", "hızlı", "teşekkür", "beğendim", "ilgili",
    "sorunsuz", "kaliteli", "mükemmel", "iyi", "beklediğim gibi", "kullanışlı",
]
NEGATIVE_WORDS = [
    "kötü", "sorun", "hata", "çöküyor", "yavaş", "pahalı", "hayal kırıklığı",
    "endişe", "tedirgin", "şüphe", "çalışmıyor", "takıl", "karışık",
    "anlamadım", "bulamadım", "geçemiyorum", "yapamıyorum", "tutmuyordu",
]


def sentiment_score(text: str) -> tuple[int, str]:
    text_lower = text.lower()
    pos_hits = sum(1 for w in POSITIVE_WORDS if w in text_lower)
    neg_hits = sum(1 for w in NEGATIVE_WORDS if w in text_lower)
    score = pos_hits - neg_hits
    if score > 0:
        return score, "Olumlu"
    if score < 0:
        return score, "Olumsuz"
    return score, "Nötr"


# ---------------------------------------------------------------------------
# 2) "Cognitive Friction" kategorileri — basit anahtar kelime tabanlı kural motoru
#    (Sprint 2 MVP kapsamı; ileride embedding tabanlı sınıflandırmaya taşınacak)
# ---------------------------------------------------------------------------
FRICTION_KEYWORDS = {
    "Güven Sorunu": ["güven", "param", "endişe", "tedirgin", "dolandır", "şüphe", "risk"],
    "UX / Kullanılabilirlik Sorunu": ["kafa karış", "karışık", "bulamadım", "anlamadım", "nasıl", "buton"],
    "Teknik Sorun": ["çöküyor", "hata", "takıl", "çalışmıyor", "giriş yapamıyorum"],
    "Fiyat / Değer Sorunu": ["fiyat", "pahalı", "yüksek"],
    "Memnuniyet (Olumlu Sinyal)": ["teşekkür", "harika", "beğendim", "hızlı", "ilgili", "sorunsuz"],
}


def detect_friction_categories(text: str) -> list[str]:
    text_lower = text.lower()
    matches = []
    for category, keywords in FRICTION_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            matches.append(category)
    return matches or ["Kategorisiz"]


def analyze_reviews(df: pd.DataFrame) -> pd.DataFrame:
    scores = []
    labels = []
    categories = []
    for review in df["review"]:
        score, label = sentiment_score(str(review))
        scores.append(score)
        labels.append(label)
        categories.append(", ".join(detect_friction_categories(str(review))))
    df = df.copy()
    df["skor"] = scores
    df["duygu"] = labels
    df["friction_kategorisi"] = categories
    return df


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------
st.title("📊 NeuroMarket AI")
st.caption("Müşteri yorumlarını aksiyon alınabilir içgörülere dönüştüren analiz platformu — MVP v0.1 (Sprint 2)")

st.divider()

uploaded_file = st.file_uploader(
    "Müşteri yorumlarını içeren CSV dosyasını yükleyin (tek sütun: `review`)",
    type=["csv"],
)

use_sample = st.checkbox("Örnek veri setini kullan (data/sample_reviews.csv)", value=uploaded_file is None)

df = None
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
elif use_sample:
    df = pd.read_csv("data/sample_reviews.csv")

if df is not None:
    if "review" not in df.columns:
        st.error("CSV dosyasında `review` adında bir sütun bulunmalıdır.")
    else:
        with st.spinner("Yorumlar analiz ediliyor..."):
            result_df = analyze_reviews(df)

        st.success(f"{len(result_df)} yorum analiz edildi.")

        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("Duygu Durumu Dağılımı")
            sentiment_counts = result_df["duygu"].value_counts()
            st.bar_chart(sentiment_counts)

        with col2:
            st.subheader("En Kritik Friction Kategorileri")
            all_categories = ", ".join(result_df["friction_kategorisi"]).split(", ")
            category_counts = Counter(all_categories)
            category_df = pd.DataFrame(
                category_counts.most_common(), columns=["Kategori", "Adet"]
            ).set_index("Kategori")
            st.bar_chart(category_df)

        st.divider()
        st.subheader("🧠 Yönetici Özeti (Rule-based, Sprint 2 MVP)")
        top_category, top_count = category_counts.most_common(1)[0]
        negative_ratio = (result_df["duygu"] == "Olumsuz").mean()
        st.markdown(
            f"""
            - Analiz edilen **{len(result_df)}** yorumun **%{negative_ratio*100:.0f}**'i olumsuz duygu içeriyor.
            - En sık karşılaşılan sorun kategorisi: **{top_category}** ({top_count} yorumda tespit edildi).
            - Bu kategori önceliklendirilerek aksiyon alınması önerilir.
            """
        )

        st.divider()
        st.subheader("📋 Detaylı Sonuçlar (Kaynak yorumlarla birlikte)")
        st.dataframe(result_df, use_container_width=True)

        st.caption(
            "Not: Duygu analizi ve friction kategorileri, Türkçe anahtar kelime tabanlı "
            "kural motoru ile hesaplanmıştır. Sprint 3'te embedding tabanlı topic "
            "clustering ve LLM destekli özet ile değiştirilecektir."
        )
else:
    st.info("Başlamak için bir CSV yükleyin ya da örnek veri setini kullanın.")
