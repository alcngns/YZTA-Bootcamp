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

## Backlog (Sprint 2'ye aktarılan)
- [ ] **Veritabanı Kurulumu** — email ile toplanacak veriler için (Kod) — Sprint Review kararıyla ertelendi
- [ ] Topic clustering geliştirme/iyileştirme (Kod)
- [ ] Sprint Review'da belirlenen ek özellikler *(detaylandırılacak)*
- [ ] Unit test yazımı — Retrospective kararıyla eklendi, önceliklendirilecek (Kod)

## To-Do
*(Sprint 1 kapandı, boş)*

## In Progress
*(Sprint 1 kapandı, boş)*

## Done
- [x] Proje iskeletinin kurulması (Kod) — Alican Güneş — 3 puan
- [x] CSV yükleme & doğrulama mantığı (Kod) — Behiye İlayda Selçuk — 5 puan
- [x] Sentiment modeli entegrasyonu — ilk versiyon (Kod) — Alican Güneş — 5 puan
- [x] Kaynak yorum eşleştirme — US-07 (Kod) — Behiye İlayda Selçuk — 3 puan
- [x] Repo + README + backlog dökümanları (Türü Olmayan Çalışma) — Behiye İlayda Selçuk — 2 puan

**Puan: 18 / Toplam Puan: 50** 

---

## Sprint Review & Retrospective Özeti
Detaylar için:
- [Sprint 1 Review](sprint_review.md)
- [Sprint 1 Retrospective](sprint_retrospective.md)

**Öne çıkan kararlar:**
- Veritabanı PBI'ı Sprint 2'ye ertelendi (form/CSV akışı için şart değildi)
- Ürün test edildi, problem görülmedi
- Görev dağılımı ve tahmin puanları gözden geçirilecek
- Unit test efor/saati artırılacak

---

**Son güncelleme:** 5 Temmuz 2026
**Güncelleyen:** Product Owner & Scrum Master
