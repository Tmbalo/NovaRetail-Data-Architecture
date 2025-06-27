# File: scripts/data_generation/generate_products.py
# This script generates sample product data for a retail application.
# It creates a variety of products across different categories with random prices.
from faker import Faker
import pandas as pd
import random



# Initialize Faker
fake = Faker()


product_categories = {
    "Electronics": ["Smartphone", "Laptop", "Tablet", "TV"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket"],
    "Furniture": ["Sofa", "Table", "Chair"],
    "Books": ["Novel", "Biography", "Textbook"]
}

data = []

for cat, items in product_categories.items():
    for item in items:
        for i in range(1, 4):
            pid = f"PROD_{fake.unique.random_int(min=100, max=999)}"
            pname = f"{item} {i}"
            price = round(random.uniform(10.00, 1000.00), 2)
            row = {
                "product_id": pid,
                "product_name": pname,
                "product_category": cat,
                "unit_price": price
            }
            data.append(row)

            # 5% chance to add a duplicate row
            if random.random() < 0.05:
                data.append(row.copy())

df = pd.DataFrame(data)
df.to_csv("data/sample_data/products.csv", index=False)
print(f"Generated {len(df)} product records.")
print(df.head())