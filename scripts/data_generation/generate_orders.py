# File: scripts/data_generation/generate_orders.py
# This script generates sample order data for a retail application.
from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()


# Load product and customer data
# This assumes you have CSV files named "products.csv" and "customers.csv" with product and customer details
product_df = pd.read_csv("data/sample_data/products.csv")
customer_df = pd.read_csv("data/sample_data/customers.csv")

# Generate order data
# Each order will have a unique ID, customer ID, product ID, unit price, total amount, order date, and region
# Simulate 1000 orders with some anomalies and duplicates
data = []
for _ in range(1000):
    cust = customer_df.sample().iloc[0]
    prod = product_df.sample().iloc[0]
    
    qty = random.randint(1, 5)
    unit_price = prod['unit_price']
    total = round(qty * unit_price, 2)
    
    # Simulate 5% negative amounts (anomalies)
    if random.random() < 0.05:
        total = -total
    
    order = {
        "order_id": fake.unique.uuid4(),
        "customer_id": cust["customer_id"],
        "product_id": prod["product_id"],
        "unit_price": unit_price,
        "total_amount": total,
        "order_date": fake.date_time_this_month(),
        "region": cust["region"],
        "email_pii": cust["email_pii"],
        "phone_pii": cust["phone_pii"]
    }
    
    # 3% chance of duplicate
    data.append(order)
    if random.random() < 0.03:
        data.append(order.copy())
        
# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("data/sample_data/orders.csv", index=False)
print(f"Generated {len(df)} order records.")
print(df.head())