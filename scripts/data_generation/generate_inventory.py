from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()
num_records = 500

# Generate inventory data
inventory = {
    "product_id": [random.randint(501, 600) for _ in range(num_records)],
    "warehouse_id": [random.randint(1, 10) for _ in range(num_records)],
    "stock_quantity": [random.randint(0, 1000) for _ in range(num_records)],
    "update_date": [fake.date_between(start_date="-30d", end_date="now") for _ in range(num_records)]
}

# Create DataFrame and save to CSV
df_inventory = pd.DataFrame(inventory)
df_inventory.to_csv("inventory_sample.csv", index=False)
print("Generated inventory_sample.csv")