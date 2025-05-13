# app.py
import streamlit as st
import joblib

# Chargement du modèle
model = joblib.load("spam_classifier.joblib")

# Interface utilisateur
st.title("📨 Détection de Spam SMS")
st.write("Entrez un message pour savoir s'il est **Spam** ou **Ham**.")

message = st.text_area("Message texte", "")

if st.button("Prédire"):
    if message.strip() == "":
        st.warning("⚠️ Veuillez entrer un message.")
    else:
        prediction = model.predict([message])[0]
        label = "📬 Ham (non-spam)" if prediction == 0 else "🚨 Spam"
        st.success(f"Résultat : **{label}**")
