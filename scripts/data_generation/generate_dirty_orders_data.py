from faker import Faker
import pandas as pd
import random
from datetime import timedelta

fake = Faker()
Faker.seed(123)

# Load customer data to link orders
customers_df = pd.read_csv("data/sample_data/dirty_customers.csv")
customer_ids = customers_df['CustomerID'].dropna().tolist()

def generate_dirty_orders_data(num_orders=200):
    data = []
    for _ in range(num_orders):
        customer_id = random.choice(customer_ids) if random.random() > 0.03 else fake.uuid4() # 3% invalid customer IDs
        order_id = fake.uuid4()
        order_date = fake.date_between(start_date='-2y', end_date='today')
        delivery_date = order_date + timedelta(days=random.randint(1,14))
        amount = round(random.uniform(50.0, 1500.0), 2)
        status = random.choice(["Shipped", "Delivered", "delivered", "Cancelled",
                                "cancelled", "cnceled", "Processing", None]) # dirty status
        payment_type = random.choice(["Credit Card", "PayPal", "Bank Transfer", "Crypto",
                                      "", "Cash"])
        notes = fake.sentence() if random.random() > 0.85 else None # 15% missing notes

        data.append({
            "OrderID": order_id,
            "CustomerID": customer_id,
            "OrderDate": order_date.strftime("%Y/%m/%d") if random.random() > 0.1 else order_date.strftime("%d-%m-%Y"), # 10% wrong datw format
            "DeliveryDate": delivery_date,
            "Amount": amount,
            "Status": status,
            "PaymentType": payment_type,
            "Notes": notes

        })

    # Introduce  some duplicates
    data.extend(random.sample(data, 10)) 

    df = pd.DataFrame(data)
    return df

df_orders = generate_dirty_orders_data(200)
df_orders.to_csv("data/sample_data/dirty_orders.csv", index=False)
print(df_orders.head())
