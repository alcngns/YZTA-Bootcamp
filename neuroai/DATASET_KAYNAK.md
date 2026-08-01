# Veri Seti Kaynağı

**Turkish Online Customer Reviews Dataset**
Kaynak: https://github.com/ozgekervan/Turkish-Online-Customer-Reviews-Dataset

- 2000 gerçek müşteri yorumu (hepsiburada.com, n11.com, trendyol.com)
- 1000 pozitif, 1000 negatif — dengeli, etiketli
- Akademik kullanım için hazırlanmıştır

## Dosyalar
- `turkish_reviews_raw.csv` — orijinal indirilen veri (Label;Text, ; ile ayrılmış)
- `customer_reviews_labeled.csv` — temizlenmiş, model eğitimi için kullanılan veri (`scripts/prepare_dataset.py` ile üretilir)
- `sample_reviews.csv` — uygulama demosu için gerçek yorumlardan seçilmiş 40 örnek (etiketsiz, `review` sütunu)

## Model
`scripts/train_model.py` bu veri setinin %80'i ile TF-IDF + Logistic Regression modelini
eğitir, kalan %20'lik test setinde **%92 doğruluk** ve **%92 F1 skoru** elde eder.
