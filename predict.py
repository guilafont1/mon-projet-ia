import sys
import joblib

def predict_message(msg):
    model = joblib.load("spam_classifier.joblib")
    prediction = model.predict([msg])[0]
    return "Spam" if prediction == 1 else "Ham"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict.py \"Your message here\"")
    else:
        msg = sys.argv[1]
        result = predict_message(msg)
        print(f"Prédiction : {result}")
