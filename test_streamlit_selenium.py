from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("🚀 Lancement du test automatique Streamlit avec Selenium...")

# Liste des messages à tester + résultat attendu
test_cases = [
    ("Win a free iPhone now!", "spam"),
    ("Hey, are you coming tonight?", "ham"),
    ("You have won $1000!", "spam"),
    ("I'll call you later.", "ham"),
    ("URGENT! Your account is at risk!", "spam"),
]

# Lancer Chrome
driver = webdriver.Chrome()
print("🌐 ChromeDriver lancé.")

try:
    # Charger Streamlit
    driver.get("http://localhost:8501")
    time.sleep(5)

    for idx, (message, expected) in enumerate(test_cases, 1):
        print(f"\n🧪 Test {idx}: '{message}' (attendu : {expected.upper()})")

        # Trouver la zone de texte
        text_area = driver.find_element(By.TAG_NAME, "textarea")
        text_area.clear()
        text_area.send_keys(message)

        # Cliquer sur le bouton
        button = driver.find_element(By.TAG_NAME, "button")
        button.click()
        time.sleep(2)

        # Lire le contenu de la page
        page_content = driver.page_source.lower()

        # Vérifier le résultat attendu
        if expected == "spam" and ("spam" in page_content or "🚨" in page_content):
            print("✅ Résultat correct : Spam détecté.")
        elif expected == "ham" and ("ham" in page_content or "📬" in page_content):
            print("✅ Résultat correct : Ham détecté.")
        else:
            print("❌ Résultat incorrect.")
            raise AssertionError(f"Test échoué pour le message : '{message}'")

    print("\n🎉 Tous les tests Selenium ont réussi.")

except Exception as e:
    print("\n❌ Une erreur est survenue :", e)

finally:
    driver.quit()
    print("🧹 Fermeture du navigateur.")
