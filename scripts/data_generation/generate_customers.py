# File: scripts/data_generation/generate_customers.py

from faker import Faker
import pandas as pd
import random

fake = Faker()
num_customers = 500
data = []

for _ in range(num_customers):
    customer_id = f"CUST_{fake.unique.random_int(min=1000, max=9999)}"
    name = fake.name()
    
    email = fake.email() if random.random() > 0.1 else None
    phone = fake.phone_number() if random.random() > 0.1 else None
    region = random.choice(["Gauteng", "Western Cape", "KwaZulu-Natal", "Eastern Cape"])
    marketing_consent = random.choice(["Yes", "No"])

    row = {
        "customer_id": customer_id,
        "customer_name": name,
        "email_pii": email,
        "phone_pii": phone,
        "region": region,
        "marketing_consent": marketing_consent
    }
    data.append(row)

    # 5% chance to add a duplicate
    if random.random() < 0.05:
        data.append(row.copy())

df = pd.DataFrame(data)
df.to_csv("data/sample_data/customers.csv", index=False)

print(f"Generated {len(df)} customer records.")
print(df.head())