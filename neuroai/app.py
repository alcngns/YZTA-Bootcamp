"""
NeuroMarket AI — Müşteri İçgörü Platformu (Sprint 3)

Sekmeler:
  🏠 Ana Sayfa   — ürün tanıtımı
  📊 Analiz      — çalışan uygulama (CSV yükle, analiz et)
  ⚙️ Nasıl Çalışır — teknik mimari (jüri/teknik okuyucular için)

Mimari:
  1) Perception: TF-IDF + Logistic Regression (eğitilmiş model, %92 doğruluk)
  2) Yapısal katman: TF-IDF + KMeans (unsupervised topic clustering)
  3) Kural motoru: cognitive friction kategorileri
  4) Advisory katman: Insight Agent — Gemini (varsa) + şablon fallback

Çalıştırmak için:
    pip install -r requirements.txt
    python scripts/prepare_dataset.py
    python scripts/train_model.py
    streamlit run app.py
"""

from collections import Counter

import joblib
import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

from insight_agent import generate_action_recommendations, generate_executive_summary

st.set_page_config(page_title="NeuroMarket AI", page_icon="🧠", layout="wide")

MODEL_PATH = "models/sentiment_pipeline.joblib"

TURKISH_STOPWORDS = [
    "ve", "bir", "bu", "da", "de", "çok", "ile", "için", "gibi", "ama",
    "ancak", "ben", "sen", "o", "biz", "siz", "onlar", "ki", "mi", "mu",
    "mü", "ne", "her", "en", "daha", "az", "içinde", "üzerine", "kadar",
]

FRICTION_KEYWORDS = {
    "Güven Sorunu": ["güven", "param", "endişe", "tedirgin", "dolandır", "şüphe", "risk"],
    "UX / Kullanılabilirlik Sorunu": ["kafa karış", "karışık", "bulamadım", "anlamadım", "nasıl", "buton"],
    "Teknik Sorun": ["çöküyor", "hata", "takıl", "çalışmıyor", "giriş yapamıyorum"],
    "Fiyat / Değer Sorunu": ["fiyat", "pahalı", "yüksek", "ucuz"],
    "Kargo / Teslimat": ["kargo", "teslimat", "gecikme", "geç geldi"],
    "Ürün Kalitesi": ["kalite", "kırık", "bozuk", "hasarlı", "ayıplı"],
}

CUSTOM_CSS = """
<style>
.hero { padding: 2.5rem 2rem; border-radius: 16px;
        background: linear-gradient(135deg, #6C5CE7 0%, #a29bfe 100%);
        color: #FFFFFF !important; margin-bottom: 1.5rem; }
.hero h1 { margin: 0 0 0.5rem 0; font-size: 2.2rem; color: #FFFFFF !important; }
.hero p { margin: 0; font-size: 1.05rem; color: #FFFFFF !important; opacity: 0.95; }
.feature-card { background: #F5F3FF; border-radius: 12px; padding: 1.2rem;
                height: 100%; border: 1px solid #E4DFFB; color: #1A1A2E !important; }
.feature-card h4 { margin-top: 0; color: #6C5CE7 !important; }
.feature-card, .feature-card * { color: #1A1A2E !important; }
.feature-card h4 { color: #6C5CE7 !important; }
</style>
"""


@st.cache_resource
def load_sentiment_model():
    return joblib.load(MODEL_PATH)


def detect_friction_categories(text: str):
    text_lower = text.lower()
    matches = [cat for cat, kws in FRICTION_KEYWORDS.items() if any(k in text_lower for k in kws)]
    return matches or ["Kategorisiz"]


def analyze_reviews(df: pd.DataFrame, model) -> pd.DataFrame:
    df = df.copy()
    df["duygu"] = model.predict(df["review"])
    proba = model.predict_proba(df["review"])
    pos_idx = list(model.classes_).index("Pozitif")
    df["guven_skoru"] = proba[:, pos_idx].round(3)
    df["friction_kategorisi"] = df["review"].apply(lambda r: ", ".join(detect_friction_categories(r)))
    return df


def cluster_topics(reviews, n_clusters: int = 4):
    n_clusters = max(2, min(n_clusters, len(reviews) // 3 or 1))
    vectorizer = TfidfVectorizer(stop_words=TURKISH_STOPWORDS, max_features=500, min_df=1)
    X = vectorizer.fit_transform(reviews)
    if X.shape[0] < n_clusters:
        return [0] * len(reviews), {0: "Tek Grup (yetersiz veri)"}
    km = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = km.fit_predict(X)
    terms = vectorizer.get_feature_names_out()
    cluster_names = {}
    for i in range(n_clusters):
        top_terms = [terms[idx] for idx in km.cluster_centers_[i].argsort()[-3:][::-1]]
        cluster_names[i] = " / ".join(top_terms)
    return labels, cluster_names


st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

tab_home, tab_analysis, tab_how = st.tabs(["🏠 Ana Sayfa", "📊 Analiz Paneli", "⚙️ Nasıl Çalışır"])

# ---------------------------------------------------------------------------
# TAB 1 — Ana Sayfa (ürün tanıtımı)
# ---------------------------------------------------------------------------
with tab_home:
    st.markdown(
        """
        <div class="hero">
          <h1>🧠 NeuroMarket AI</h1>
          <p>Dağınık müşteri yorumlarını, işletmeler için aksiyon alınabilir ürün ve
          hizmet iyileştirme raporlarına dönüştürüyoruz.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write(
        "NeuroMarket AI, müşteri yorumlarını analiz ederek duygu durumu, tekrar eden "
        "şikayetler, kullanıcı deneyimi sorunları ve güven problemlerini tespit eden "
        "yapay zekâ destekli bir müşteri içgörü platformudur. Yorumları yalnızca "
        "olumlu/olumsuz olarak etiketlemekle kalmaz — **hangi konuda, neden ve nasıl** "
        "bir aksiyon alınması gerektiğini gerçek yorum örnekleriyle birlikte sunar."
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            '<div class="feature-card"><h4>🎯 Duygu Analizi</h4>'
            "Gerçek veriyle eğitilmiş model, %92 doğrulukla yorumları sınıflandırır.</div>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            '<div class="feature-card"><h4>🧩 Konu Kümeleme</h4>'
            "Yorumları otomatik olarak benzer konulara göre gruplar.</div>",
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            '<div class="feature-card"><h4>💡 Aksiyon Önerileri</h4>'
            "Yapay zekâ destekli yönetici özeti ve somut iyileştirme önerileri sunar.</div>",
            unsafe_allow_html=True,
        )

    st.write("")
    st.subheader("Hedef Kitle")
    st.write("Mobil uygulama geliştiren şirketler · E-ticaret markaları · Restoran/hizmet "
             "sektörü işletmeleri · Ürün yöneticileri ve müşteri deneyimi (CX) ekipleri")

    st.info("👉 Başlamak için üstteki **📊 Analiz Paneli** sekmesine geçin.")

# ---------------------------------------------------------------------------
# TAB 2 — Analiz Paneli (asıl çalışan araç)
# ---------------------------------------------------------------------------
with tab_analysis:
    try:
        model = load_sentiment_model()
    except FileNotFoundError:
        st.error(
            "Eğitilmiş model bulunamadı. Önce şu komutları çalıştırın:\n\n"
            "```\npython scripts/prepare_dataset.py\npython scripts/train_model.py\n```"
        )
        st.stop()

    uploaded_file = st.file_uploader(
        "Müşteri yorumlarını içeren CSV dosyasını yükleyin (tek sütun: `review`)",
        type=["csv"],
    )
    use_sample = st.checkbox("Örnek veri setini kullan (gerçek e-ticaret yorumlarından, 40 adet)", value=uploaded_file is None)

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
                result_df = analyze_reviews(df, model)
                cluster_labels, cluster_names = cluster_topics(result_df["review"].tolist())
                result_df["konu_kumesi"] = [cluster_names[c] for c in cluster_labels]

            all_categories = ", ".join(result_df["friction_kategorisi"]).split(", ")
            category_counts = Counter(all_categories)
            top_category, top_count = category_counts.most_common(1)[0]
            neg_ratio = (result_df["duygu"] == "Negatif").mean()

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Toplam Yorum", len(result_df))
            m2.metric("Olumsuz Oran", f"%{neg_ratio*100:.0f}")
            m3.metric("En Kritik Kategori", top_category)
            m4.metric("Bu Kategoride", f"{top_count} yorum")

            st.write("")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Duygu Durumu Dağılımı")
                st.bar_chart(result_df["duygu"].value_counts())
            with col2:
                st.subheader("Kritik Friction Kategorileri")
                cat_df = pd.DataFrame(category_counts.most_common(), columns=["Kategori", "Adet"]).set_index("Kategori")
                st.bar_chart(cat_df)

            st.subheader("Otomatik Konu Kümeleri")
            st.bar_chart(result_df["konu_kumesi"].value_counts())

            stats = {
                "total": len(result_df),
                "negative_ratio": neg_ratio,
                "top_category": top_category,
                "top_category_count": top_count,
            }
            example_negative = result_df[result_df["duygu"] == "Negatif"]["review"].head(8).tolist()

            st.divider()
            sum_col, rec_col = st.columns(2)
            with sum_col:
                st.subheader("🧠 Yönetici Özeti")
                st.markdown(generate_executive_summary(stats, example_negative))
            with rec_col:
                st.subheader("💡 Aksiyon Önerileri")
                st.markdown(generate_action_recommendations(stats, example_negative))

            st.divider()
            with st.expander("📋 Detaylı Sonuçlar (kaynak yorumlarla birlikte)"):
                st.dataframe(
                    result_df[["review", "duygu", "guven_skoru", "friction_kategorisi", "konu_kumesi"]],
                    width="stretch",
                )
    else:
        st.info("Başlamak için bir CSV yükleyin ya da örnek veri setini kullanın.")

# ---------------------------------------------------------------------------
# TAB 3 — Nasıl Çalışır (teknik detay, ana ekranı kirletmesin diye ayrı sekmede)
# ---------------------------------------------------------------------------
with tab_how:
    st.subheader("Sistem Mimarisi")
    st.markdown(
        """
        1. **Perception katmanı** — TF-IDF + Logistic Regression ile eğitilmiş duygu
           analizi modeli (2000 gerçek Türkçe e-ticaret yorumuyla eğitildi, **%92 test
           doğruluğu**).
        2. **Yapısal katman** — TF-IDF + KMeans ile unsupervised konu kümeleme.
        3. **Kural motoru** — "cognitive friction" kategorileri (güven, UX, teknik sorun,
           fiyat, kargo, ürün kalitesi) anahtar kelime tabanlı olarak işaretlenir.
        4. **Advisory katman (Insight Agent)** — Google Gemini API ile yönetici özeti ve
           aksiyon önerileri üretilir; API anahtarı tanımlı değilse otomatik olarak
           şablon tabanlı bir özet/öneriye düşülür (uygulama asla çökmez).
        """
    )
    st.subheader("Veri Kaynağı")
    st.write(
        "Turkish Online Customer Reviews Dataset — 2000 gerçek müşteri yorumu "
        "(hepsiburada.com, n11.com, trendyol.com), akademik kullanım için hazırlanmış. "
        "Detaylar: `data/DATASET_KAYNAK.md`"
    )
    