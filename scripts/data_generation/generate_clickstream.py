from faker import Faker
import json
import random
from datetime import datetime, timedelta

fake = Faker()
num_records = 1000

# Generate clickstream data
clickstream = [
    {
        "user_id": str(random.randint(1001, 2000)),
        "session_id": fake.uuid4(),
        "page_views": random.sample(["home", "product_page", "cart", "checkout"], k=random.randint(1, 4)),
        "timestamp": fake.date_time_between(start_date="-30d", end_date="now").isoformat(),
        "session_duration": random.randint(60, 600)
    }
    for _ in range(num_records)
]

# Save to JSON
with open("clickstream_sample.json", "w") as f:
    json.dump(clickstream, f, indent=4)
print("Generated clickstream_sample.json")