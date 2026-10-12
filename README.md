# ✉️ Projet IA — Sujet 06 : Classification Automatique d'Emails (SPAM vs NON-SPAM)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4%2B-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red.svg)
![NLP](https://img.shields.io/badge/NLP-TF--IDF%20%7C%20Stopwords-green.svg)
![Dataset](https://img.shields.io/badge/Dataset-5200%20Emails%20en%20Français-brightgreen.svg)

---

## 📌 Présentation du Projet

Ce projet s'inscrit dans le cadre du **Sujet 06 d'IA** portant sur la **détection automatique de courriers indésirables (SPAM / Phishing / Arnaques)** dans des emails en français.

Il combine une **étude méthodologique complète en Notebook Jupyter**, une évaluation rigoureuse de **trois algorithmes de Machine Learning** (Naive Bayes, SVM Linéaire, Random Forest), et la mise en disposition d'une **application web interactive Streamlit (`MailGuard`)** permettant de tester l'analyse d'emails en temps réel.

---

## 📊 Jeu de Données (`french_email_dataset_5k.csv`)

Afin d'offrir une grande représentativité du trafic email francophone tout en respectant la confidentialité (RGPD), nous avons constitué un corpus de **5 200 emails en français** :

- **Taille totale :** 5 200 messages.
- **Répartition des classes :** Parfaitement équilibrée — **2 600 SPAM** et **2 600 NON-SPAM** (50 % / 50 %).
- **Partition d'évaluation :**
  - **Jeu d'entraînement (Train - 80%) :** 4 160 emails (2 080 spam, 2 080 non-spam)
  - **Jeu de test (Test - 20%) :** 1 040 emails (520 spam, 520 non-spam)
- **Types de contenus couverts :**
  - **Légitimes (NON-SPAM) :** Communications d'entreprise, comptes-rendus de projets, échanges RH, factures, billets de train/avion, réservations, newsletters d'actualité.
  - **Indésirables (SPAM) :** Phishing bancaire/carte vitale/colis bloqué en douane, arnaques d'héritage, opportunités d'investissement crypto miracle, spams commerciaux agressifs et contrefaçons.

---

## 🏆 Résultats & Performances des Modèles

Les trois algorithmes prescrits par les consignes du Sujet 06 ont été évalués de manière strictement étanche sur le même jeu de test de **1 040 emails** (sans fuite de données) :

| Modèle                                          | Exactitude (Accuracy) | Précision SPAM | Rappel (Recall) SPAM | Score F1 SPAM | Nb d'erreurs (sur 1040) |   AUC ROC   |
| :---------------------------------------------- | :-------------------: | :------------: | :------------------: | :-----------: | :---------------------: | :---------: |
| 🥇 **Multinomial Naive Bayes (Optimisé)**       |      **99,90 %**      |  **99,81 %**   |     **100,0 %**      |  **0,9990**   |          **1**          | **1.0000**  |
| 🥈 **SVM Linéaire (`LinearSVC`)**               |      **99,81 %**      |  **99,62 %**   |     **100,0 %**      |  **0,9981**   |          **2**          | **0.99999** |
| 🥉 **Random Forest (`RandomForestClassifier`)** |      **99,71 %**      |  **99,43 %**   |     **100,0 %**      |  **0,9971**   |          **3**          | **1.0000**  |

> 💡 **Constat clé :** Les 3 modèles atteignent un **Rappel (Recall) SPAM de 100,0 %**, garantissant qu'aucun email dangereux ou tentative de phishing n'est laissé passer dans la boîte de réception principale.

---

## 📁 Architecture du Dépôt GitHub

```text
Projet_IA_Sujet_06/
├── README.md                             <-- Présentation complète du projet
├── .gitignore                            <-- Fichiers ignorés par Git
├── french_email_dataset_5k.csv           <-- Dataset de 5 200 emails en français
├── Projet_IA_S06_notebook.ipynb          <-- Notebook Jupyter d'expérimentation & IA
├── Rapport_Projet_IA_Sujet_06.docx       <-- Rapport technique  (Word)
├── Sujets-IA.pdf                          <-- Document officiel du sujet
└── Interface_Detection_Spam/              <-- Application Web Streamlit
    ├── app.py                            <-- Code source de l'interface MailGuard
    ├── requirements.txt                  <-- Dépendances Python
    └── README.txt                        <-- Guide d'exécution de l'interface
```

---

## 💻 Installation & Lancement Rapide

### 1. Prérequis

Assurez-vous d'avoir installé **Python 3.10 ou supérieur** et **Git**.

### 2. Cloner le projet

```bash
git clone https://github.com/Mahfouz17/Projet_IA_Sujet_06.git
cd Projet_IA_Sujet_06
```

### 3. Lancer l'Application Web Streamlit (`MailGuard`)

```bash
# Aller dans le dossier de l'interface
cd Interface_Detection_Spam

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'interface web
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse **`http://localhost:8501`**.

---

## 🔬 Méthodologie NLP & Pipeline de Prétraitement

1. **Nettoyage Textuel :** Conversion en minuscules, suppression de la ponctuation et filtrage des mots vides (_stopwords_) en français via NLTK.
2. **Vectorisation TF-IDF :** Pondération par fréquence de terme et inverse de fréquence documentaire (`ngram_range=(1, 2)` pour capturer les unigrammes et les bigrammes).
3. **Validation Croisée & Optimisation :** Réalisation d'une validation croisée à 5 folds (`StratifiedKFold`) et d'un réglage des hyperparamètres par `GridSearchCV`.

---

## 📄 Livrables & Documentation

- **Rapport Synthétique (Word) :** [`Rapport_Projet_IA_Sujet_06.docx`](Rapport_Projet_IA_Sujet_06.docx)

- **Notebook d'Expérimentation :** [`Projet_IA_S06_notebook.ipynb`](Projet_IA_S06_notebook.ipynb)

---

## 👤 Auteurs & Projet Académique

- **Auteur :** Cheikh Mafou Aidara (Étudiant en Informatique)
- **GitHub :** [@Mahfouz17](https://github.com/Mahfouz17)
- **Projet :** Réalisé dans le cadre du cours d'**Intelligence Artificielle — Sujet 06**.
