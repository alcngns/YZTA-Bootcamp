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
# Sprint 1 — Sprint Review

**Tarih:** 5 Temmuz 2026
**Sprint Review Katılımcıları:** Behiye İlayda Selçuk (Product Owner), Alican Güneş (Scrum Master)

## Alınan Kararlar
- Email ile toplanacak veriler için ayrı bir veritabanı oluşturulmasının gerekli olduğu görülmüştür.
  Ancak bu veritabanı, mevcut CSV yükleme (form) sayfasının çalışması için şart değildir.
  Bu nedenle ilgili PBI (**Veritabanı Kurulumu — email verisi toplama**) bir sonraki sprint'e
  aktarılmıştır.
- Ortaya çıkan üründe (CSV yükleme + sentiment analizi ilk versiyonu) çalışma ve testler
  sırasında herhangi bir problem gözlemlenmemiştir.
- Ekstra olarak eklenmesi gereken özellikler belirlenmiştir (bkz. "Sprint 2'ye Aktarılanlar").

## Sprint 1'de Tamamlanan
- Proje iskeletinin kurulması
- CSV yükleme & doğrulama mantığı
- Sentiment analizi (ilk versiyon)
- Kaynak yorum eşleştirme (US-07)

## Sprint 2'ye Aktarılanlar
- Veritabanı kurulumu (email üzerinden toplanan verilerin saklanması için)
- Topic clustering'in geliştirilmesi/iyileştirilmesi
- Review sürecinde belirlenen ek özellikler *(detaylandırılacak — Sprint 2 planlamasında backlog'a eklenecek)*


# Sprint 1 — Sprint Retrospective

**Tarih:** 5 Temmuz 2026
**Katılımcılar:** Behiye İlayda Selçuk (Product Owner), Alican Güneş (Scrum Master)

## Alınan Kararlar / Aksiyon Maddeleri
- Takım içindeki görev dağılımıyla ilgili düzenleme yapılması kararı alınmıştır.
- Tahmin puanları (story point) gözden geçirilmeli; sprint planlama toplantılarında
  developer'ların gerekli geri bildirimi verdiğinden emin olunmalıdır.
- Unit test'ler için ayrılan efor/saat artırılmalıdır.

## Sprint 2'ye Etkisi
- Sprint 2 planlamasında görev dağılımı yeniden gözden geçirilecek.
- Story point tahminleri, ekip geri bildirimiyle birlikte yeniden değerlendirilecek.
- Backlog'a "Unit test yazımı" için ayrı task'ler eklenecek ve bu task'lere daha fazla
  efor/saat ayrılacak.

**Öne çıkan kararlar:**
- Veritabanı PBI'ı Sprint 2'ye ertelendi (form/CSV akışı için şart değildi)
- Ürün test edildi, problem görülmedi
- Görev dağılımı ve tahmin puanları gözden geçirilecek
- Unit test efor/saati artırılacak

---

**Son güncelleme:** 5 Temmuz 2026
**Güncelleyen:** Product Owner & Scrum Master
