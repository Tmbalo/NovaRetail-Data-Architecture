from faker import Faker
import pandas as pd
from datetime import datetime, timedelta
import random

fake = Faker()
num_records = 1000

# Generate orders data
orders = {
    "order_id": range(1, num_records + 1),
    "customer_id": [random.randint(1001, 2000) for _ in range(num_records)],
    "product_id": [random.randint(501, 600) for _ in range(num_records)],
    "order_date": [fake.date_time_between(start_date="-30d", end_date="now") for _ in range(num_records)],
    "total_amount": [round(random.uniform(10.0, 500.0), 2) for _ in range(num_records)],
    "region": [random.choice(["US", "EU", "APAC"]) for _ in range(num_records)]
}

# Create DataFrame and save to CSV
df_orders = pd.DataFrame(orders)
df_orders.to_csv("orders_sample.csv", index=False)
print("Generated orders_sample.csv")