import pandas as pd
import random

def generate_churn_data(n_customers=3000):
    print(f"Generating {n_customers} customer records for the ISP...")
    data = []

    for customer_id in range(1, n_customers + 1):
        # Müşteri Profil Özellikleri
        tenure_months = random.randint(1, 72)
        internet_type = random.choice(['Fiber Optic', 'DSL'])
        contract = random.choice(['Month-to-month', 'One year', 'Two year'])

        # Finansal Bilgiler
        base_bill = 45 if internet_type == 'DSL' else 85
        monthly_bill = base_bill + random.uniform(-10, 25)
        monthly_bill = round(monthly_bill, 2)
        total_charges = round(tenure_months * monthly_bill, 2)

        # Müşteri Deneyimi ve Şikayetler
        tech_support_calls = random.randint(0, 5) if tenure_months > 12 else random.randint(0, 8)
        speed_drops = random.randint(0, 3)

        # --- CHURN (TERK ETME) ALGORİTMASI ---
        churn_probability = 0.10 # Temel ayrılma ihtimali

        if contract == 'Month-to-month':
            churn_probability += 0.25 # Taahhütsüzler kolay kaçar
        if tech_support_calls > 3:
            churn_probability += 0.30 # Çok arıza kaydı bırakanlar sinirlidir
        if internet_type == 'Fiber Optic' and monthly_bill > 95:
            churn_probability += 0.15 # Pahalı fatura ödeyenler alternatif arar
        if tenure_months > 48:
            churn_probability -= 0.20 # Eski müşteriler sadıktır

        # Olasılığı 0 ile 1 arasına sabitleme
        churn_probability = max(0.0, min(1.0, churn_probability))

        # 1 = Müşteri Ayrıldı (Churn), 0 = Müşteri Kaldı
        is_churn = 1 if random.random() < churn_probability else 0

        data.append([
            f"CUST-{customer_id:04d}", tenure_months, internet_type, contract,
            monthly_bill, total_charges, tech_support_calls, speed_drops, is_churn
        ])

    columns = [
        "CustomerID", "Tenure_Months", "Internet_Type", "Contract",
        "Monthly_Bill", "Total_Charges", "Tech_Support_Calls", "Speed_Drops", "Churn"
    ]

    df = pd.DataFrame(data, columns=columns)
    df.to_csv("isp_churn_data.csv", index=False)
    print("✅ 'isp_churn_data.csv' successfully created!")
    return df

if __name__ == "__main__":
    generate_churn_data()