"""
NeuroMarket AI — Unit Testleri

Çalıştırmak için:
    pip install pytest
    pytest tests/
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import joblib
import pytest

from app import analyze_reviews, cluster_topics, detect_friction_categories

MODEL_PATH = "models/sentiment_pipeline.joblib"


@pytest.fixture(scope="module")
def model():
    return joblib.load(MODEL_PATH)


class TestFrictionCategories:
    def test_guven_sorunu_tespit_edilir(self):
        result = detect_friction_categories("param gitti mi bilmiyorum çok endişeliyim")
        assert "Güven Sorunu" in result

    def test_teknik_sorun_tespit_edilir(self):
        result = detect_friction_categories("uygulama sürekli çöküyor giriş yapamıyorum")
        assert "Teknik Sorun" in result

    def test_kategori_yoksa_kategorisiz_doner(self):
        result = detect_friction_categories("bugün hava çok güzel")
        assert result == ["Kategorisiz"]

    def test_birden_fazla_kategori_donebilir(self):
        result = detect_friction_categories("kargo çok geç geldi ve ürün kırık geldi")
        assert "Kargo / Teslimat" in result
        assert "Ürün Kalitesi" in result


class TestSentimentModel:
    def test_belirgin_pozitif_yorum_dogru_siniflandirilir(self, model):
        pred = model.predict(["harika bir ürün kesinlikle tavsiye ederim çok memnun kaldım"])
        assert pred[0] == "Pozitif"

    def test_belirgin_negatif_yorum_dogru_siniflandirilir(self, model):
        pred = model.predict(["berbat bir ürün kesinlikle tavsiye etmiyorum çok pişmanım"])
        assert pred[0] == "Negatif"

    def test_analyze_reviews_gerekli_kolonlari_uretir(self, model):
        import pandas as pd

        df = pd.DataFrame({"review": ["harika bir ürün", "berbat bir deneyim"]})
        result = analyze_reviews(df, model)
        for col in ["duygu", "guven_skoru", "friction_kategorisi"]:
            assert col in result.columns
        assert set(result["duygu"]) <= {"Pozitif", "Negatif"}


class TestTopicClustering:
    def test_kucuk_veri_setinde_tek_grup_doner(self):
        labels, names = cluster_topics(["kısa yorum bir", "kısa yorum iki"])
        assert len(set(labels)) >= 1
        assert len(names) >= 1

    def test_kume_sayisi_veri_setinden_fazla_olamaz(self):
        reviews = ["ürün güzel"] * 3 + ["kargo geç geldi"] * 3
        labels, names = cluster_topics(reviews, n_clusters=10)
        assert len(names) <= len(reviews)
