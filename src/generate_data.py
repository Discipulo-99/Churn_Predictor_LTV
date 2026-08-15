import os
import numpy as np
import pandas as pd

# Crear estructura de carpetas si no existe
os.makedirs("data", exist_ok=True)
os.makedirs("notebooks", exist_ok=True)
os.makedirs("src", exist_ok=True)

np.random.seed(42)
n_samples = 2500

customer_id = [f"CUST-{1000 + i}" for i in range(n_samples)]
tenure_months = np.random.randint(1, 72, size=n_samples)
contract_type = np.random.choice(['Month-to-Month', 'One Year', 'Two Year'], size=n_samples, p=[0.55, 0.25, 0.20])
payment_method = np.random.choice(['Electronic Check', 'Mailed Check', 'Bank Transfer', 'Credit Card'], size=n_samples, p=[0.40, 0.20, 0.20, 0.20])

monthly_charges = np.round(np.random.uniform(20.0, 120.0, size=n_samples), 2)
tech_support_tickets = np.random.poisson(lam=1.8, size=n_samples)
days_since_last_login = np.random.randint(0, 45, size=n_samples)
discount_used = np.random.choice([0, 1], size=n_samples, p=[0.65, 0.35])

score_churn = (
    0.45 * (contract_type == 'Month-to-Month') +
    0.25 * (tech_support_tickets > 2) +
    0.20 * (days_since_last_login > 20) +
    0.15 * (monthly_charges > 75) -
    0.30 * (tenure_months > 24) -
    0.20 * (contract_type == 'Two Year') +
    np.random.normal(0, 0.15, size=n_samples)
)

prob_churn = 1 / (1 + np.exp(-score_churn))
churn_label = (prob_churn > 0.50).astype(int)

total_charges = np.round(monthly_charges * tenure_months * np.random.uniform(0.9, 1.05, size=n_samples), 2)

future_ltv_12m = np.where(
    churn_label == 1,
    np.round(monthly_charges * np.random.uniform(0.5, 2.0, size=n_samples), 2),
    np.round(monthly_charges * 12 * np.random.uniform(0.85, 1.15, size=n_samples), 2)
)

df = pd.DataFrame({
    'CustomerID': customer_id,
    'TenureMonths': tenure_months,
    'ContractType': contract_type,
    'PaymentMethod': payment_method,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges,
    'TechSupportTickets': tech_support_tickets,
    'DaysSinceLastLogin': days_since_last_login,
    'DiscountUsed': discount_used,
    'Churn': churn_label,
    'FutureLTV_12M': future_ltv_12m
})

df.to_csv("data/raw/random_raw_customer_data.csv", index=False)
print("Dataset guardado con éxito en 'data/raw/random_raw_customer_data.csv'")