from faker import Faker
import json
import random
from datetime import datetime, timedelta

fake = Faker()
num_records = 1000
product_categories = {
    "Electronics": ["TV", "Laptop", "Phone"],
    "Home Appliances": ["Fridge", "Microwave", "Washer"],
    "Furniture": ["Sofa", "Table", "Chair"],
    "Clothing": ["Shirt", "Jeans", "Jacket"]
}
products = []
product_id = 501
for category, names in product_categories.items():
    for name in names:
        products.append({"product_id": product_id, "product_name": f"{name} {random.randint(100, 999)}", "product_category": category})
        product_id += 1

clickstream = [
    {
        "user_id": random.randint(1001, 2000),  # Matches customer_id
        "session_id": f"session_{i}",
        "page_views": random.randint(1, 10),
        "product_id": random.choice(products)["product_id"],
        "product_name": random.choice(products)["product_name"],
        "product_category": random.choice(products)["product_category"],
        "timestamp": fake.date_time_between(start_date="-30d", end_date="now").isoformat(),
        "session_duration_seconds": random.randint(60, 3600)
    }
    for i in range(num_records)
]

with open("data/sample_data/clickstream_sample.json", "w") as f:
    json.dump(clickstream, f, indent=2)
print("Generated clickstream_sample.json")