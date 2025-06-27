# File: scripts/data_generation/generate_products.py
# This script generates sample product data for a retail application.

from faker import Faker
import pandas as pd
import random

fake = Faker()
# Define product categories and their items
# Each category has a list of items, and each item will have 3 versions
product_categories = {
    "Electronics": ["Smartphone", "Laptop", "Tablet", "TV"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket"],
    "Furniture": ["Sofa", "Table", "Chair"],
    "Books": ["Novel", "Biography", "Textbook"]
}

# Generate product data
# Each product will have a unique ID, name, category, and price
data = []
product_id_set = set()
for cat, items in product_categories.items():
    for item in items:
        for i in range(1, 4):  # 3 versions per item
            pid = f"PROD_{fake.unique.random_int(min=100, max=999)}"
            pname = f"{item} {i}"
            price = round(random.uniform(10.00, 1000.00), 2)
            data.append({
                "product_id": pid,
                "product_name": pname,
                "product_category": cat,
                "unit_price": price
            })
            product_id_set.add(pid)
            
# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("data/sample_data/products.csv", index=False)
print(f"Generated {len(product_id_set)} product records.")
print(df.head())