# MailGuard — Classification des emails SPAM / NON-SPAM

Prototype pédagogique réalisé avec Python, scikit-learn et Streamlit.

## Fichiers

- `app.py` : interface web Streamlit.
- `train_model.py` : entraîne un pipeline TF-IDF + Multinomial Naive Bayes avec GridSearchCV.
- `model.joblib` : pipeline entraîné chargé par l'application.
- `french_email_dataset_5k.csv` : corpus français utilisé pour entraîner le modèle.
- `requirements.txt` : dépendances Python.

## Lancer en local

Python 3.10 ou plus récent est recommandé.

```bash
python -m venv .venv
```

Activation de l'environnement :

- Windows PowerShell : ` .\.venv\Scripts\Activate.ps1 `
- macOS/Linux : `source .venv/bin/activate`

Puis :

```bash
pip install -r requirements.txt
python train_model.py
streamlit run app.py
```

Ouvrez l'adresse locale affichée dans le terminal.

## Déployer sur Streamlit Community Cloud

1. Poussez tous les fichiers du projet sur un dépôt GitHub.
2. Connectez-vous à Streamlit Community Cloud avec GitHub.
3. Créez une application et sélectionnez le dépôt, la branche et `app.py` comme fichier principal.
4. Déployez l'application.

## À propos des résultats

Le script entraîne un modèle sur le corpus complet avec une recherche d'hyperparamètres par validation croisée. Le score affiché par `train_model.py` est un score moyen de validation croisée ; ce n'est pas le score du jeu de test du notebook. Pour citer les résultats expérimentaux du rapport, utilisez les mesures calculées séparément sur le jeu de test.

Ce prototype ne garantit pas la détection de tous les spams. Évitez d'y coller des emails confidentiels ou contenant des données personnelles.
