## **Takım İsmi**

**Takım 111** 

# Ürün İle İlgili Bilgiler

# NeuroMarket AI

## Takım İsmi
**NeuroMarket AI Ekibi** *(YZTA Bootcamp 2026 — 5. Akademi Dönemi)*

## Takım Elemanları / Rolleri

| İsim | Rol |
|---|---|
| Behiye İlayda Selçuk | Product Owner |
| Behiye İlayda Selçuk | Developer |
| Alican Güneş | Scrum Master |
| Alican Güneş | Developer |


## Ürün İsmi
**NeuroMarket AI**

## Ürün İle İlgili Bilgiler

### Ürün Açıklaması
NeuroMarket AI, işletmelerin müşteri yorumlarını (mobil uygulama, e-ticaret, restoran vb.) analiz ederek
duygu durumu, tekrar eden şikayetler, kullanıcı deneyimi sorunları, güven problemleri ve kafa karışıklığı
yaratan noktaları tespit eden yapay zekâ destekli bir müşteri içgörü (customer insight) platformudur.

Sistem yorumları yalnızca olumlu/olumsuz olarak sınıflandırmakla kalmaz; **hangi konuda, neden ve nasıl**
bir aksiyon alınması gerektiğini, gerçek yorum örnekleriyle desteklenmiş şekilde işletmelere sunar.

**Değer Önerisi:** *"Dağınık müşteri yorumlarını, işletmeler için aksiyon alınabilir ürün ve hizmet
iyileştirme raporlarına dönüştürüyoruz."*

### Ürün Özellikleri
- CSV / metin tabanlı müşteri yorumu yükleme
- Sentiment (duygu durumu) analizi
- Topic clustering (konu bazlı gruplama)
- "Cognitive friction" — kullanıcı sürtünmesi kategorileri (kafa karışıklığı, güven sorunu, UX problemi vb.)
- En kritik şikayet alanlarının önceliklendirilmesi
- LLM destekli yönetici özeti (executive summary)
- Aksiyon önerileri (recommendation)
- Örnek yorumlarla kanıt gösterimi (traceability)
- Dashboard üzerinden görselleştirme

### Hedef Kitle
- Mobil uygulama geliştiren şirketler
- E-ticaret markaları
- Restoran / hizmet sektörü işletmeleri
- Ürün yöneticileri ve müşteri deneyimi (CX) ekipleri


## Teknoloji Yığını (Öneri — geliştirme sürecinde netleşecek)
- Backend: Python (FastAPI)
- NLP/AI: HuggingFace transformers, sentiment/topic modeling, LLM (özet + öneri ajanı)
- Veritabanı: PostgreSQL
- Frontend/Dashboard: React veya Streamlit
- Deployment: Docker

## Lisans / Kapsam
Bu proje YZTA (Yapay Zeka ve Teknoloji Akademisi) Bootcamp 2026 kapsamında, ekip tarafından sıfırdan
geliştirilmektedir. Hazır proje, satın alma veya dışarıdan destek kullanılmamaktadır.

## Product Backlog 

---

# Sprint 1

- **Sprint içinde tamamlanması tahmin edilen puan**: 50 Puan

- **Puan tamamlama mantığı**: Proje boyunca tamamlanması gereken toplam 150 puanlık backlog bulunmaktadır. 3 sprinte bölündüğünde ilk sprintin 50 ile başlaması gerektiği kararlaştırıldı.

- **Daily Scrum**: Daily Scrum toplantılarının Google Meet üzerinden yapılması kararlaştırılmıştır. Toplantı ekran görüntülerimiz DailyScrum klasörü içindedir.

- # Sprint 1 — Board

## Rejected
*(şu an yok)*

## To-Do
*(Sprint 1 kapandı, boş)*

## In Progress
*(Sprint 1 kapandı, boş)*

## Done
- [x] Veri seti araştırılmasına başlandı. — Alican Güneş — 10 puan
- [x] Sistem mimarisi belirlendi. — Behiye İlayda Selçuk — 10 puan
- [x] Kullanılacak teknolojiler belirlendi. — Alican Güneş — 10 puan
- [x] Sentiment/NLP kütüphaneleri için ön araştırma  — Behiye İlayda Selçuk — 10 puan
- [x] Repo + README + backlog dökümanları (Türü Olmayan Çalışma) — Behiye İlayda Selçuk — 10 puan

**Puan: 50 / Toplam Puan: 150** 

---

## Sprint Review & Retrospective Özeti

# Sprint 1 — Sprint Review

**Tarih:** 5 Temmuz 2026
**Sprint Review Katılımcıları:** Behiye İlayda Selçuk (Product Owner), Alican Güneş (Scrum Master)

## Alınan Kararlar
- Veri setleri arttırılmalı.
- Sistem mimarisi tekrardan gözden geçirilip eksik kısımlar tamamlanmalı.
- Ekstra olarak eklenmesi gereken özellikler belirlenmiştir.

## Sprint 1'de Tamamlanan
- Proje iskeletinin kurulması
- Veri seti araştırılması
- Görev dağılımı

# Sprint 1 — Sprint Retrospective

**Tarih:** 5 Temmuz 2026
**Katılımcılar:** Behiye İlayda Selçuk (Product Owner), Alican Güneş (Scrum Master)

## Alınan Kararlar / Aksiyon Maddeleri
- Takım içindeki görev dağılımıyla ilgili düzenleme yapılması kararı alınmıştır.
- Tahmin puanları (story point) gözden geçirilmeli; sprint planlama toplantılarında
  developer'ların gerekli geri bildirimi verdiğinden emin olunmalıdır.
- Unit test'ler için ayrılan efor/saat artırılmalıdır.
- Sistem mimarisi iyileştirilmeli.


**Öne çıkan kararlar:**
- Veri setleri detaylandırılacak.
- Görev dağılımı ve tahmin puanları gözden geçirilecek
- Unit test efor/saati artırılacak

---

# Sprint 2

- **Sprint içinde tamamlanması tahmin edilen puan**: 60 Puan
- **Puan tamamlama mantığı**: Sprint 1'de tamamlanan araştırma ve mimari çalışmaların üzerine, gerçek
  ürün geliştirme işleri bu sprintte hayata geçirilmiştir. Sprint Review'da alınan "veri setleri
  artırılmalı" ve "sistem mimarisi gözden geçirilmeli" kararları da bu sprint kapsamında ele alınmıştır.
  

## Sprint 2 — Board

## Rejected
*(şu an yok)*

## To-Do
*(Sprint 2 kapandı, boş)*

## In Progress
*(Sprint 2 kapandı, boş)*

## Done
- [x] CSV yükleme & doğrulama mantığının geliştirilmesi (US-01) — Behiye İlayda Selçuk — 10 puan
- [x] Türkçe anahtar kelime tabanlı duygu analizi motoru (US-02) — Alican Güneş — 15 puan
- [x] Cognitive friction kategorilendirmesi (US-03) — Alican Güneş — 15 puan
- [x] Kritik alan önceliklendirme + kaynak yorum gösterimi (US-04) — Behiye İlayda Selçuk — 10 puan
- [x] Streamlit dashboard arayüzü (US-05) — Behiye İlayda Selçuk & Alican Güneş — 10 puan

**Puan: 60 / Toplam Puan: 150**

---

## Sprint 2 — Sprint Review

**Tarih:** 5 Temmuz - 19 Temmuz
**Sprint Review Katılımcıları:** Behiye İlayda Selçuk (Product Owner), Alican Güneş (Scrum Master)

### Alınan Kararlar
- Duygu analizi için Türkçe destekli bir kural motoru geliştirilmiştir (İngilizce odaklı
  kütüphanelerin Türkçe metinlerde yetersiz kaldığı görülmüştür).
- Veri seti sayısı Sprint 1'deki review kararına uygun şekilde artırılmıştır.
- Sistem mimarisi gözden geçirilerek dashboard katmanı netleştirilmiştir.
- Ekstra özellik olarak "cognitive friction" kategorilendirmesi MVP'ye dahil edilmiştir.

### Sprint 2'de Tamamlanan
- Çalışan bir MVP (CSV yükleme + duygu analizi + kategori + dashboard)
- Sprint 1'den kalan veri seti ve mimari eksiklerinin giderilmesi

## Sprint 2 — Sprint Retrospective

**Tarih:** 19 Temmuz 2026
**Katılımcılar:** Behiye İlayda Selçuk (Product Owner), Alican Güneş (Scrum Master)

### Alınan Kararlar / Aksiyon Maddeleri
- Unit test yazımı bu sprintte planlanmış ancak önceliklendirme nedeniyle Sprint 3'e taşınmıştır.
- Veritabanı kurulumu (email verisi için), LLM destekli özet ve deployment Sprint 3'e aktarılmıştır.
- Görev dağılımı bu sprintte dengeli şekilde uygulanmıştır; bu yaklaşım korunacaktır.

---
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
- [x] `insight_agent.py` — LLM destekli özet modülü (Gemini API, fallback'li)

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
- Yönetici özeti için LLM entegrasyonu (Gemini API) eklenmiş, API erişimi olmayan
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


**Son güncelleme:** 01.08.2026
**Güncelleyen:** Product Owner & Scrum Master

