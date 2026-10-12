"""Entraîne le pipeline TF-IDF + MultinomialNB et sauvegarde model.joblib."""
from pathlib import Path
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "french_email_dataset_5k.csv"
MODEL_PATH = ROOT / "model.joblib"


def main():
    df = pd.read_csv(DATA_PATH).dropna(subset=["text", "label"])
    X = df["text"].astype(str)
    y = df["label"].astype(str).str.strip().str.lower()

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("model", MultinomialNB()),
    ])
    params = {
        "tfidf__min_df": [1, 2, 3],
        "tfidf__ngram_range": [(1, 1), (1, 2)],
        "model__alpha": [0.1, 0.5, 1.0],
    }
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    search = GridSearchCV(pipeline, params, cv=cv, scoring="accuracy", n_jobs=-1)
    search.fit(X, y)
    joblib.dump(search.best_estimator_, MODEL_PATH)
    print(f"Modèle sauvegardé : {MODEL_PATH}")
    print(f"Meilleurs paramètres : {search.best_params_}")
    print(f"Accuracy moyenne en validation croisée : {search.best_score_:.4%}")
    print("Note : ce score CV n'est pas l'accuracy du jeu de test du notebook.")

if __name__ == "__main__":
    main()
