from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()
num_records = 500
product_categories = {
    "Electronics": ["TV", "Laptop", "Phone"],
    "Home Appliances": ["Fridge", "Microwave", "Washer"],
    "Furniture": ["Sofa", "Table", "Chair"],
    "Clothing": ["Shirt", "Jeans", "Jacket"]
}

# Generate enough products to meet num_records
products = []
product_id = 501  # Start at 501 to align with orders/clickstream
base_products = [
    {"name": name, "category": category}
    for category, names in product_categories.items()
    for name in names
]
while len(products) < num_records:
    for base in base_products:
        if len(products) < num_records:
            products.append({
                "product_id": product_id,
                "product_name": f"{base['name']} {random.randint(1001, 9999)}",
                "product_category": base['category']
            })
            product_id += 1

# Ensure products list matches num_records
products = products[:num_records]

# Generate inventory data
inventory = {
    "product_id": [p["product_id"] for p in products],
    "product_name": [p["product_name"] for p in products],
    "product_category": [p["product_category"] for p in products],
    "unit_price": [round(random.uniform(10.0, 500.0), 2) for _ in range(num_records)],
    "warehouse_id": [random.randint(1, 10) for _ in range(num_records)],
    "warehouse_name": [f"Warehouse_{random.randint(1, 10)}" for _ in range(num_records)],
    "warehouse_region": [random.choice(["US", "EU", "APAC"]) for _ in range(num_records)],
    "employee_count": [random.randint(10, 100) for _ in range(num_records)],
    "stock_quantity": [random.randint(0, 1000) for _ in range(num_records)],
    "update_date": [fake.date_time_between(start_date="-30d", end_date="now") for _ in range(num_records)]
}

df_inventory = pd.DataFrame(inventory)
df_inventory.to_csv("data/sample_data/inventory_sample.csv", index=False)
print("Generated inventory_sample.csv")