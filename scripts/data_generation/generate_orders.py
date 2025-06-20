from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()
num_records = 1000
# Define product categories and names
product_categories = {
    "Electronics": ["TV", "Laptop", "Phone"],
    "Home Appliances": ["Fridge", "Microwave", "Washer"],
    "Furniture": ["Sofa", "Table", "Chair"],
    "Clothing": ["Shirt", "Jeans", "Jacket"]
}

# Generate product IDs and names with consistent categories
products = []
product_id = 501
for category, names in product_categories.items():
    for name in names:
        products.append({"product_id": product_id, "product_name": f"{name} {random.randint(100, 999)}", "product_category": category})
        product_id += 1

orders = {
    "order_id": range(1, num_records + 1),
    "customer_id": [random.randint(1001, 2000) for _ in range(num_records)],
    "customer_name": [fake.name() for _ in range(num_records)],
    "email_pii": [fake.email() for _ in range(num_records)],
    "phone_pii": [fake.phone_number() for _ in range(num_records)],
    "product_id": [random.choice(products)["product_id"] for _ in range(num_records)],
    "product_name": [random.choice(products)["product_name"] for _ in range(num_records)],
    "product_category": [random.choice(products)["product_category"] for _ in range(num_records)],
    "unit_price": [round(random.uniform(10.0, 500.0), 2) for _ in range(num_records)],
    "order_date": [fake.date_time_between(start_date="-30d", end_date="now") for _ in range(num_records)],
    "total_amount": [round(random.uniform(10.0, 500.0), 2) for _ in range(num_records)],
    "region": [random.choice(["US", "EU", "APAC"]) for _ in range(num_records)]
}

df_orders = pd.DataFrame(orders)
df_orders.to_csv("data/sample_data/orders_sample.csv", index=False)
print("Generated orders_sample.csv")