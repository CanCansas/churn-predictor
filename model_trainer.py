import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib


def train_churn_model():
    print("Loading the ISP customer dataset...")
    try:
        df = pd.read_csv("isp_churn_data.csv")
    except FileNotFoundError:
        print("Error: 'isp_churn_data.csv' not found. Run data_generator.py first.")
        return

    # 1. Data Preprocessing (Veri Ön İşleme)
    print("Preprocessing data and dropping unnecessary columns...")

    # CustomerID (Müşteri No) tahmin yaparken işimize yaramaz, onu siliyoruz
    X = df.drop(["Churn", "CustomerID"], axis=1)  # Features (Özellikler)
    y = df["Churn"]  # Target variable (Hedefimiz: Müşteri ayrıldı mı? 1/0)

    # Yapay zeka metin anlamaz, 'Fiber Optic' veya 'Month-to-month' gibi metinleri sayılara çeviriyoruz
    X_encoded = pd.get_dummies(X, drop_first=True)

    # 2. Train-Test Split (Verinin %80'i eğitim, %20'si test için ayrılır)
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    # 3. Model Training (Model Eğitimi - Sınıflandırma)
    print("Training the AI model (Random Forest Classifier)...")
    # class_weight="balanced" ile yapay zekanın azınlıkta olan ayrılan müşterileri daha iyi yakalamasını sağlıyoruz
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")
    model.fit(X_train, y_train)

    # 4. Model Evaluation (Modelin Başarısını Ölçme)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print("\n--- MODEL PERFORMANCE REPORT ---")
    print(f"✅ Accuracy Score (Doğruluk Oranı): {accuracy * 100:.2f}%")
    print("--------------------------------\n")

    # 5. Modeli Kaydetme (Streamlit panelinde kullanmak için beyni kaydediyoruz)
    print("Saving the model's brain...")
    joblib.dump(model, "churn_model.pkl")
    joblib.dump(X_encoded.columns, "churn_columns.pkl")
    print("🎉 Success! 'churn_model.pkl' has been created.")


if __name__ == "__main__":
    train_churn_model()