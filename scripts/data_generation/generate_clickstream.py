
# File: scripts/data_generation/generate_clickstream.py   
# This script generates clickstream data for a retail application, simulating user sessions with page views, session duration, and product interactions.
# It uses Faker to create realistic timestamps and randomizes session attributes.

import json
import random
from faker import Faker

import pandas as pd

# Initialize Faker
fake = Faker()

# Load product and customer data
# This assumes you have CSV files named "products.csv" and "customers.csv" with product and customer details        
product_df = pd.read_csv("data/sample_data/products.csv")
customer_df = pd.read_csv("data/sample_data/customers.csv")

sessions = []
for _ in range(2000):
    prod = product_df.sample().iloc[0]
    cust = customer_df.sample().iloc[0]

    session = {
        "user_id": cust["customer_id"],
        "session_id": fake.uuid4(),
        "page_views": random.randint(1, 15),
        "session_duration_seconds": random.randint(5, 1800),
        "product_id": prod["product_id"],
        "product_name": prod["product_name"],
        "product_category": prod["product_category"],
        "timestamp": fake.date_time_this_month().isoformat()
    }

    sessions.append(session)

with open("data/sample_data/clickstream.json", "w") as f:
    for session in sessions:
        f.write(json.dumps(session) + "\n")
        
        
print(f"Generated {len(sessions)} clickstream records.")
# Display the first few records
df = pd.DataFrame(sessions)
print(df.head())
