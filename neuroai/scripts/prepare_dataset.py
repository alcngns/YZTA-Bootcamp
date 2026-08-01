"""
Veri setini hazırlama scripti.

Kaynak: Turkish Online Customer Reviews Dataset (ozgekervan)
https://github.com/ozgekervan/Turkish-Online-Customer-Reviews-Dataset
2000 gerçek müşteri yorumu (hepsiburada.com, n11.com, trendyol.com) — Pozitif/Negatif etiketli.
Akademik kullanım için hazırlanmıştır (bkz. data/DATASET_KAYNAK.md).

Çalıştırma:
    python scripts/prepare_dataset.py
"""

import pandas as pd

RAW_PATH = "data/turkish_reviews_raw.csv"
LABELED_OUT = "data/customer_reviews_labeled.csv"
SAMPLE_OUT = "data/sample_reviews.csv"


def main():
    df = pd.read_csv(RAW_PATH, sep=";", encoding="utf-8")
    df = df.rename(columns={"Text": "review", "Label": "sentiment_gt"})
    df["sentiment_gt"] = df["sentiment_gt"].map({True: "Pozitif", False: "Negatif"})
    df = df.dropna(subset=["review"]).drop_duplicates(subset=["review"])

    # Model eğitimi için etiketli tam veri seti
    df[["review", "sentiment_gt"]].to_csv(LABELED_OUT, index=False)
    print(f"Etiketli veri seti kaydedildi: {LABELED_OUT} ({len(df)} satır)")

    # Uygulama demosu için etiketsiz örnek alt küme (gerçek yorumlardan, karışık pozitif/negatif)
    sample = pd.concat(
        [
            df[df["sentiment_gt"] == "Pozitif"].sample(20, random_state=42),
            df[df["sentiment_gt"] == "Negatif"].sample(20, random_state=42),
        ]
    ).sample(frac=1, random_state=42)  # karıştır
    sample[["review"]].to_csv(SAMPLE_OUT, index=False)
    print(f"Demo örnek veri seti kaydedildi: {SAMPLE_OUT} ({len(sample)} satır)")


if __name__ == "__main__":
    main()
