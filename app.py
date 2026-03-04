import streamlit as st
import pandas as pd
import joblib

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Customer Churn AI", page_icon="📊", layout="centered")


# --- LOAD AI MODEL ---
@st.cache_resource
def load_model():
    try:
        model = joblib.load("churn_model.pkl")
        model_columns = joblib.load("churn_columns.pkl")
        return model, model_columns
    except FileNotFoundError:
        return None, None


model, model_columns = load_model()

# --- HEADER ---
st.title("📊 ISP Customer Churn Predictor")
st.markdown("Enter customer details below to predict the probability of them leaving the service to a competitor.")
st.markdown("---")

if model is None:
    st.error("⚠️ Model files not found! Please run 'model_trainer.py' first.")
else:
    # --- USER INPUT FORM ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Customer Profile")
        tenure_months = st.slider("Tenure (Months with us)", 1, 72, 12)
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        internet_type = st.selectbox("Internet Service", ["Fiber Optic", "DSL"])

    with col2:
        st.subheader("Usage & Support")
        monthly_bill = st.number_input("Monthly Bill ($)", min_value=10.0, max_value=200.0, value=65.0, step=1.0)
        tech_support_calls = st.slider("Tech Support Calls", 0, 10, 1)
        speed_drops = st.slider("Speed Drops (per month)", 0, 5, 0)

    st.markdown("---")

    # --- PREDICTION LOGIC ---
    if st.button("🔍 Predict Churn Risk", use_container_width=True):
        with st.spinner("AI is analyzing customer behavior..."):

            # Arka planda toplam harcamayı hesapla
            total_charges = tenure_months * monthly_bill

            # Kullanıcı verisini DataFrame'e çevir
            input_data = pd.DataFrame([{
                "Tenure_Months": tenure_months,
                "Internet_Type": internet_type,
                "Contract": contract,
                "Monthly_Bill": monthly_bill,
                "Total_Charges": total_charges,
                "Tech_Support_Calls": tech_support_calls,
                "Speed_Drops": speed_drops
            }])

            # Veriyi modelin anladığı formata (0 ve 1'lere) dönüştür
            input_encoded = pd.get_dummies(input_data)
            input_aligned = input_encoded.reindex(columns=model_columns, fill_value=0)

            # Tahmin Yap!
            prediction = model.predict(input_aligned)[0]
            probability = model.predict_proba(input_aligned)[0][1]  # Churn olma ihtimali

            # --- DISPLAY RESULTS ---
            st.subheader("AI Analysis Result:")
            if prediction == 1:
                st.error(f"🚨 HIGH RISK: This customer is likely to CHURN! (Probability: {probability * 100:.1f}%)")
                st.info(
                    "💡 Recommendation: Offer a customized discount, waive equipment fees, or contact customer support immediately to retain them.")
            else:
                st.success(
                    f"✅ LOW RISK: This customer is likely to STAY. (Probability of leaving: {probability * 100:.1f}%)")
                st.info("💡 Recommendation: Standard retention policies apply. No urgent action needed.")