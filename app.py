from pathlib import Path
import joblib
import streamlit as st

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "model.joblib"

st.set_page_config(page_title="MailGuard | Détection de spam", page_icon="✉️", layout="centered")
st.markdown("""
<style>
.stApp {background:#f5faf6;}
.block-container {max-width:900px;padding-top:2rem;}
.hero {background:#075b3b;color:white;padding:26px 28px;border-radius:18px;margin-bottom:18px;}
.hero h1 {color:white;margin:0;font-size:2.1rem;}
.hero p {color:#e5f4eb;margin:.5rem 0 0;}
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="hero"><h1>MailGuard</h1><p>Classification automatique des emails — SPAM ou NON-SPAM</p></div>', unsafe_allow_html=True)
st.write("Collez le contenu d'un email pour obtenir une prédiction du modèle de Machine Learning.")

@st.cache_resource(show_spinner="Chargement du modèle…")
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("model.joblib absent. Exécutez d'abord : python train_model.py")
    return joblib.load(MODEL_PATH)

try:
    model = load_model()
    email = st.text_area(
        "Contenu de l'email",
        height=220,
        placeholder="Ex. : Félicitations, vous avez gagné un cadeau. Cliquez ici pour en profiter…",
    )
    if st.button("Analyser l'email", type="primary", use_container_width=True):
        if not email.strip():
            st.warning("Saisissez d'abord le contenu d'un email.")
        else:
            prediction = str(model.predict([email])[0]).strip().lower()
            st.divider()
            if prediction == "spam":
                st.error("Résultat du modèle : SPAM")
            elif prediction in {"non-spam", "ham", "not spam"}:
                st.success("Résultat du modèle : NON-SPAM")
            else:
                st.info(f"Classe prédite par le modèle : {prediction}")
            st.caption("Prototype pédagogique : une prédiction automatique n'est pas une garantie de sécurité.")
except Exception as exc:
    st.error("Le modèle n'a pas pu être chargé.")
    st.code(str(exc))

st.caption("Projet IA — Sujet 06 · MailGuard · Les textes saisis ne sont pas enregistrés par ce code.")
