from faker import Faker
import pandas as pd
import random

fake = Faker()
Faker.seed(42)

print("Starting")
def generate_dirty_customer_data (num_records=100):
    data = []
    for _ in range(num_records):
        # Simulate random missing values and dirty entries
        name = fake.name() if random.random() > 0.5 else None # 5% missing names
        email = fake.email() if random.random() > 0.1 else fake.user_name() + "@gmail" # 10% malformed
        phone = fake.phone_number() if random.random() > 0.1 else str(fake.random_int(min=1000000, max=9999999)) # some missing area codes
        birthdate = fake.date_of_birth(minimum_age=18, maximum_age=80)
        join_date = fake.date_between(start_date='-3y', end_date='today')
        status = random.choice(["active", "inactive", "Active", "INACTIVE", "actve"]) # inconsistent values

        data.append({
            "CustomerID": fake.uuid4(),
            "Name": name,
            "Email": email,
            "Phone": phone,
            "BirthDate": birthdate,
            "JoinDate": join_date,
            "Status": status
        })

    # Introduce duplicates
    data.extend(random.sample(data, 5))

    df = pd.DataFrame(data)
    return df
    
df_dirty = generate_dirty_customer_data(100)
df_dirty.to_csv("data/sample_data/dirty_customers.csv", index=False)
print(df_dirty.head())
print("Generated dirty_customers.csv")
