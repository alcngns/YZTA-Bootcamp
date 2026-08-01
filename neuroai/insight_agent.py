"""
Insight Agent — Gemini destekli yönetici özeti ve aksiyon önerisi üretici.

GEMINI_API_KEY tanımlıysa (.env dosyasından okunur) Google Gemini API'sini kullanarak
gerçek bir LLM özeti/öneri üretir. Tanımlı değilse veya API çağrısı başarısız olursa
otomatik olarak şablon tabanlı bir üretime düşer (fallback) — kullanıcıya asla ham API
hata mesajı gösterilmez, teknik detaylar yalnızca konsola (terminale) yazdırılır.

Kurulum:
    1) .env.example dosyasını .env olarak kopyalayın
    2) https://aistudio.google.com adresinden ücretsiz bir Gemini API anahtarı alın
    3) .env dosyasına GEMINI_API_KEY=... şeklinde yapıştırın
    (.env dosyası .gitignore'da olduğu için repo'ya asla yüklenmez)
"""

import os

from dotenv import load_dotenv

load_dotenv()

# Google modelleri sık değiştiriyor; "-latest" alias'ı otomatik olarak en güncel Flash
# modeline yönlendirilir. Yine de olası kesintilere karşı sırayla denenecek yedek liste.
MODEL_CANDIDATES = ["gemini-flash-latest", "gemini-2.5-flash-lite", "gemini-2.0-flash"]


def _get_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or "buraya_kendi" in api_key:
        return None
    try:
        from google import genai
        return genai.Client(api_key=api_key)
    except Exception as e:
        print(f"[Insight Agent] Gemini client oluşturulamadı: {e}")
        return None


def _call_gemini(client, prompt: str) -> str | None:
    """Model listesini sırayla dener, ilk çalışanın yanıtını döner. Hepsi başarısız
    olursa None döner (teknik detaylar sadece konsola yazılır, kullanıcıya gösterilmez)."""
    for model_name in MODEL_CANDIDATES:
        try:
            response = client.models.generate_content(model=model_name, contents=prompt)
            return response.text
        except Exception as e:
            print(f"[Insight Agent] '{model_name}' başarısız, sıradaki denenecek: {e}")
            continue
    print("[Insight Agent] Tüm Gemini modelleri başarısız oldu, şablon özet kullanılıyor.")
    return None


def _fallback_summary(stats: dict) -> str:
    return (
        f"- Analiz edilen **{stats['total']}** yorumun **%{stats['negative_ratio']*100:.0f}**'i "
        f"olumsuz duygu içeriyor.\n"
        f"- En sık karşılaşılan sorun kategorisi: **{stats['top_category']}** "
        f"({stats['top_category_count']} yorumda tespit edildi).\n"
        f"- Bu kategori önceliklendirilerek aksiyon alınması önerilir."
    )


def _fallback_recommendations(stats: dict) -> str:
    return (
        f"- **{stats['top_category']}** kategorisindeki yorumlar incelenerek kök neden analizi yapılmalı.\n"
        f"- Olumsuz yorum oranı %{stats['negative_ratio']*100:.0f} — bu segmentteki müşterilerle "
        f"iletişime geçilmesi önerilir."
    )


def generate_executive_summary(stats: dict, example_reviews: list) -> str:
    client = _get_client()
    if client is None:
        return _fallback_summary(stats)

    examples_text = "\n".join(f"- {r}" for r in example_reviews[:8])
    prompt = f"""Sen bir müşteri deneyimi analistisin. Aşağıdaki verilere dayanarak bir
işletme yöneticisi için 3-4 cümlelik, aksiyon odaklı bir özet yaz. Sadece verilen
verilere dayan, uydurma istatistik ekleme.

İstatistikler:
- Toplam yorum sayısı: {stats['total']}
- Olumsuz yorum oranı: %{stats['negative_ratio']*100:.0f}
- En sık sorun kategorisi: {stats['top_category']} ({stats['top_category_count']} yorumda)

Örnek yorumlar:
{examples_text}

Yanıtını Türkçe, madde işaretli ve aksiyon önerisi içerecek şekilde yaz."""

    result = _call_gemini(client, prompt)
    return result if result else _fallback_summary(stats)


def generate_action_recommendations(stats: dict, example_reviews: list) -> str:
    client = _get_client()
    if client is None:
        return _fallback_recommendations(stats)

    examples_text = "\n".join(f"- {r}" for r in example_reviews[:8])
    prompt = f"""Aşağıdaki müşteri şikayetlerine dayanarak bir ürün ekibi için 3 somut,
uygulanabilir aksiyon önerisi yaz. Her öneri tek cümle olsun ve hangi soruna karşılık
geldiğini belirt.

En sık sorun kategorisi: {stats['top_category']} ({stats['top_category_count']} yorumda tespit edildi)

Örnek şikayetler:
{examples_text}

Türkçe ve madde işaretli yanıt ver."""

    result = _call_gemini(client, prompt)
    return result if result else _fallback_recommendations(stats)