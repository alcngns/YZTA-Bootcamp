"""
NeuroMarket AI — Duygu Analizi Modeli Eğitimi

TF-IDF (kelime + karakter n-gram) + Logistic Regression ile Türkçe müşteri yorumları
üzerinde ikili (pozitif/negatif) duygu sınıflandırma modeli eğitir.

Veri seti: data/customer_reviews_labeled.csv (1968 gerçek müşteri yorumu)
Kaynak: Turkish Online Customer Reviews Dataset (ozgekervan / GitHub)

Çalıştırma:
    python scripts/train_model.py
"""

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

DATA_PATH = "data/customer_reviews_labeled.csv"
MODEL_PATH = "models/sentiment_pipeline.joblib"

# Basit Türkçe stopword listesi (sklearn'de hazır Türkçe listesi yok)
TURKISH_STOPWORDS = [
    "ve", "bir", "bu", "da", "de", "çok", "ile", "için", "gibi", "ama",
    "ancak", "ben", "sen", "o", "biz", "siz", "onlar", "ki", "mi", "mu",
    "mü", "ne", "her", "en", "daha", "az", "içinde", "üzerine", "kadar",
]


def main():
    df = pd.read_csv(DATA_PATH)
    X = df["review"]
    y = df["sentiment_gt"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(
            stop_words=TURKISH_STOPWORDS,
            ngram_range=(1, 2),
            min_df=2,
            max_features=8000,
        )),
        ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, pos_label="Pozitif")

    print(f"Test doğruluğu (accuracy): {acc:.3f}")
    print(f"F1 skoru (Pozitif sınıf): {f1:.3f}")
    print("\nDetaylı rapor:\n", classification_report(y_test, y_pred))

    joblib.dump(pipeline, MODEL_PATH)
    print(f"\nModel kaydedildi: {MODEL_PATH}")


if __name__ == "__main__":
    main()
