# Sprint 3 (Son Sprint)

- **Sprint içinde tamamlanması tahmin edilen puan**: 40 Puan
- **Puan tamamlama mantığı**: Sprint 2'de kurulan MVP üzerine, ürünü teslim edilebilir hale
  getirecek son işler bu sprintte tamamlanmıştır: gerçek veri seti ile model eğitimi, konu
  kümeleme, LLM destekli özet altyapısı.

## Sprint 3 — Yapılan İşler

| Task | Puan | Açıklama |
|---|---|---|
| Gerçek Türkçe veri seti entegrasyonu | 10 | 2000 gerçek e-ticaret yorumu (hepsiburada, n11, trendyol) — bkz. `data/DATASET_KAYNAK.md` |
| Duygu analizi modelinin eğitilmesi | 15 | TF-IDF + Logistic Regression, **%92 test doğruluğu** (`scripts/train_model.py`) |
| Konu kümeleme (topic clustering) | 5 | TF-IDF + KMeans ile unsupervised kümeleme, otomatik küme adlandırma |
| Insight Agent (LLM destekli özet) | 5 | Claude API ile gerçek LLM özeti, API key yoksa şablon fallback |
| Unit test yazımı | 5 | *(bkz. aşağıdaki not)* |

**Puan: 40 / Toplam Puan: 150** ✅ (150/150 tamamlandı)

## Sprint 3 — Board

## Done
- [x] `data/turkish_reviews_raw.csv` — 2000 gerçek yorum indirildi ve entegre edildi
- [x] `scripts/prepare_dataset.py` — veri temizleme ve hazırlama pipeline'ı
- [x] `scripts/train_model.py` — TF-IDF + Logistic Regression eğitim scripti (%92 doğruluk, %92 F1)
- [x] `models/sentiment_pipeline.joblib` — eğitilmiş model artifact'i
- [x] `app.py` — gerçek model + TF-IDF/KMeans konu kümeleme + Insight Agent entegrasyonu
- [x] `insight_agent.py` — LLM destekli özet modülü (Claude API, fallback'li)

## Ürün Mimarisi (Final)
```
Ham veri (2000 gerçek yorum)
        │
        ▼
prepare_dataset.py  →  customer_reviews_labeled.csv
        │
        ▼
train_model.py  →  TF-IDF + Logistic Regression  →  sentiment_pipeline.joblib
        │
        ▼
app.py (Streamlit)
   ├── Perception: eğitilmiş model → duygu tahmini + güven skoru
   ├── Yapısal katman: TF-IDF + KMeans → otomatik konu kümeleri
   ├── Kural motoru: cognitive friction kategorileri
   └── Insight Agent: Claude API (varsa) → yönetici özeti, yoksa şablon özet
```

Bu mimari, projenin başındaki "sadece klasik ML modeli kullanmak yetersiz kalır" öngörüsüne
uygun olarak kurgulanmıştır: küçük **eğitilmiş bir model** (perception) + **LLM destekli
advisory katman** (Insight Agent) birlikte çalışır.

## Sprint 3 — Sprint Review

**Tarih:** *(teslim tarihini yazın)*
**Katılımcılar:** Behiye İlayda Selçuk (Product Owner), Alican Güneş (Scrum Master)

### Alınan Kararlar
- Kural tabanlı duygu analizi motoru, gerçek veri setiyle eğitilmiş bir ML modeliyle
  değiştirilmiştir (%92 doğruluk).
- Topic clustering, anahtar kelime kategorilerinin yanına unsupervised bir ML yöntemiyle
  (TF-IDF + KMeans) eklenmiştir.
- Yönetici özeti için LLM entegrasyonu (Claude API) eklenmiş, API erişimi olmayan
  demo ortamları için şablon tabanlı bir yedek mekanizma korunmuştur.

### Sprint 3'te Tamamlanan
- Ürün, Sprint 1'deki tema kısıtlaması olmayan ancak zorunlu AI bileşenlerini (eğitilmiş
  model + LLM destekli katman) içeren final haline getirilmiştir.

## Sprint 3 — Sprint Retrospective

**Tarih:** *(teslim tarihini yazın)*
**Katılımcılar:** Behiye İlayda Selçuk (Product Owner), Alican Güneş (Scrum Master)

### Alınan Kararlar / Aksiyon Maddeleri
- Proje boyunca en büyük öğrenim, kural tabanlı yaklaşımların (ör. TextBlob, sözlük tabanlı
  duygu analizi) Türkçe metinlerde yetersiz kaldığı ve gerçek veriyle eğitilmiş modellerin
  şart olduğu oldu.
- GitHub push/collaborator süreçlerinde yaşanan yetkilendirme sorunları erken sprintlerde
  netleştirilmeliydi; bir sonraki projede takım kurulumunun ilk gününde bu kontrol edilecek.

---

**Son güncelleme:** *(push ettiğiniz gün buraya tarih ekleyin)*
**Güncelleyen:** Product Owner & Scrum Master
