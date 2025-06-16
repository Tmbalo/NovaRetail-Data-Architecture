from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()
num_records = 500
categories = ["Electronics", "Home Appliances", "Furniture", "Clothing"]

# Generate inventory data
inventory = {
    "product_id": [random.randint(501, 600) for _ in range(num_records)],
    "product_name": [fake.word(ext_word_list=["TV", "Sofa", "Laptop", "Shirt"]) + " " + str(random.randint(100, 999)) for _ in range(num_records)],
    "product_category": [random.choice(categories) for _ in range(num_records)],
    "unit_price": [round(random.uniform(10.0, 500.0), 2) for _ in range(num_records)],
    "warehouse_id": [random.randint(1, 10) for _ in range(num_records)],
    "warehouse_name": [fake.company() + " Warehouse" for _ in range(num_records)],
    "warehouse_region": [random.choice(["US", "EU", "APAC"]) for _ in range(num_records)],
    "employee_count": [random.randint(10, 100) for _ in range(num_records)],
    "stock_quantity": [random.randint(0, 1000) for _ in range(num_records)],
    "update_date": [fake.date_between(start_date="-30d", end_date="now") for _ in range(num_records)]
}

# Create DataFrame and save to CSV
df_inventory = pd.DataFrame(inventory)
df_inventory.to_csv("data/sample_data/inventory_sample.csv", index=False)
print("Generated inventory_sample.csv")