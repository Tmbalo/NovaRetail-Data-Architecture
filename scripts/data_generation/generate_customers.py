from faker import Faker
import pandas as pd
import random

fake = Faker()
num_customers = 500

data = []
for _ in range(num_customers):
    customer_id = f"CUST_{fake.unique.random_int(min=1000, max=9999)}"
    name = fake.name()
    
    # 10% chance of null email/phone
    email = fake.email() if random.random() > 0.1 else None
    phone = fake.phone_number() if random.random() > 0.1 else None

    region = random.choice(["Gauteng", "Western Cape", "KwaZulu-Natal", "Eastern Cape"])
    
    # Optional: GDPR flag
    marketing_consent = random.choice(["Yes", "No"])

    data.append({
        "customer_id": customer_id,
        "customer_name": name,
        "email_pii": email,
        "phone_pii": phone,
        "region": region,
        "marketing_consent": marketing_consent
    })

df = pd.DataFrame(data)
df.to_csv("data/sample_data/customers.csv", index=False)
print(f"Generated {num_customers} customer records.")
print(df.head())