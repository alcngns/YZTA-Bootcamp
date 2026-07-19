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

**Tarih:** * 19 Temmuz 2026
**Katılımcılar:** Behiye İlayda Selçuk (Product Owner), Alican Güneş (Scrum Master)

### Alınan Kararlar / Aksiyon Maddeleri
- Unit test yazımı bu sprintte planlanmış ancak önceliklendirme nedeniyle Sprint 3'e taşınmıştır.
- Veritabanı kurulumu (email verisi için), LLM destekli özet ve deployment Sprint 3'e aktarılmıştır.
- Görev dağılımı bu sprintte dengeli şekilde uygulanmıştır; bu yaklaşım korunacaktır.

---

**Son güncelleme:** 19 Temmuz 2026
**Güncelleyen:** Product Owner & Scrum Master

