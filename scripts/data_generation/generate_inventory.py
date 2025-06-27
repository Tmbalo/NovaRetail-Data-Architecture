# File: scripts/data_generation/generate_inventory.py
# This script generates sample inventory data for a retail application. 
from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Set random seed for reproducibility
Faker.seed(456) 
random.seed(456)


# Define warehouse IDs and their regions
# Each warehouse has a unique ID and a region
warehouse_ids = ["WH1", "WH2", "WH3", "WH4"]
warehouse_regions = {
    "WH1": "Gauteng",
    "WH2": "Western Cape",
    "WH3": "KwaZulu-Natal",
    "WH4": "Eastern Cape"
}

# Load product data from CSV
# This assumes you have a CSV file named "products.csv" with product details
product_df = pd.read_csv("data/sample_data/products.csv")

data = []
for _, row in product_df.iterrows():
    for wh_id in warehouse_ids:
        qty = random.randint(-10, 500)  # <0 for anomaly
        data.append({
            "product_id": row['product_id'],
            "product_name": row['product_name'],
            "product_category": row['product_category'],
            "warehouse_id": wh_id,
            "warehouse_name": f"{wh_id}_Main",
            "warehouse_region": warehouse_regions[wh_id],
            "employee_count": random.randint(5, 100),
            "stock_quantity": qty,
            "update_date": fake.date_this_month(),
            "unit_price": row['unit_price']
        })


df = pd.DataFrame(data)
df.to_csv("data/sample_data/inventory.csv", index=False)
print(f"Generated {len(df)} inventory records.")
print(df.head())