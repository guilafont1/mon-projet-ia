import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Charger les données
df = pd.read_csv("spam.csv", encoding="ISO-8859-1")[["v1", "v2"]]
df.columns = ["label", "message"]

# Encoder les étiquettes
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# Split données
X_train, X_test, y_train, y_test = train_test_split(df["message"], df["label"], test_size=0.2, random_state=42)

# Pipeline vectorisation + modèle
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

# Entraînement
model.fit(X_train, y_train)

# Sauvegarde
joblib.dump(model, "spam_classifier.joblib")

print("Modèle entraîné et sauvegardé.")


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Prédictions sur les données de test
y_pred = model.predict(X_test)

# Affichage des scores
print("\n✅ Évaluation du modèle :\n")
print("Accuracy :", accuracy_score(y_test, y_pred))
print("\nClassification Report :")
print(classification_report(y_test, y_pred, target_names=["Ham", "Spam"]))
print("\nMatrice de confusion :")
print(confusion_matrix(y_test, y_pred))
