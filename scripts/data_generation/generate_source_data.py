import pandas as pd
import random
from faker import Faker
from datetime import datetime
import json

# Initialize Faker
fake = Faker()
Faker.seed(456)
random.seed(456)

# Load customer data to link orders
customersid_df = pd.read_csv("customers_dirty.csv")
customer_ids = customersid_df['CustomerID'].dropna().tolist()

# Load products data to link orders(ProductID)
productid_df = pd.read_csv("products_dirty.csv")
product_ids = productid_df['ProductID'].dropna().tolist()


def generate_products(n=50):
    return pd.DataFrame({
        "ProductID": [f"P{i+1:04d}" for i in range(n)],
        "ProductName": [fake.word().capitalize() + " " + fake.color_name() for _ in range(n)],
        "Category": [random.choice(["Electronics", "Books", "Clothing", "Home", "Toys"]) for _ in range(n)],
        "Price": [round(random.uniform(10, 500), 2) for _ in range(n)]
    })


# Generate Orders Dataset
def generate_orders(n=500):
    data = []
    for i in range(n):
        customer_id = random.choice(customer_ids)
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 5)
        ##price = product_price
        #total = price * quantity
        order_date = fake.date_time_between(start_date='-3M', end_date='now')
        data.append({
            "OrderID": f"O{i+1:05d}",
            "CustomerID": customer_id,
            "ProductID": product_id,
            "Quantity": quantity,
            "TotalAmount": "pricequantity",
            "OrderDate": order_date.strftime("%Y-%m-%d %H:%M:%S")
        })
    return pd.DataFrame(data)

# Generate Clickstream Dataset
num_records = 1000
clickstream = [
    {
        "user_id": random.choice(customer_ids),
        "ProductID": random.choice(product_ids),
        "session_id":  fake.uuid4(),
         "Action": random.choice(["view", "add_to_cart", "remove_from_cart", "checkout", "search"]),
        "timestamp": fake.date_time_between(start_date="-30d", end_date="now").isoformat(),
        "session_duration_seconds": random.randint(60, 600)  # Duration in seconds
    }
    for _ in range(num_records)
]

# Generate Inventory Dataset
def generate_inventory(products):
    data = []
    for _, row in products.iterrows():
        data.append({
            "ProductID": row["ProductID"],
            "StockLevel": random.randint(0, 300),
            "ReorderLevel": random.randint(20, 100),
            "LastRestockDate": fake.date_between(start_date="-6M", end_date="-7d").strftime("%Y-%m-%d"),
            "Supplier": fake.company()
        })
    return pd.DataFrame(data)

# Main execution
if __name__ == "__main__":

    products_df = generate_products() # This is used by the inventory function

    orders_df = generate_orders()
    # Inject missing and invalid references in orders
    orders_df.loc[0, 'CustomerID'] = 'C99999' # Invalid customer
    orders_df.loc[1, 'ProductID'] = 'P0000' # Invalid product
    orders_df.loc[2, 'Quantity'] = -3 # Negative quantity
    orders_df.loc[3, 'OrderDate'] = 'not_a_date' # Invalid datetime
    orders_df = pd.concat([orders_df, orders_df.iloc[[4]]]) # Duplicate row


    inventory_df = generate_inventory(products_df)
    # Inject stock outlier and date issue
    inventory_df.loc[0, 'StockLevel'] = -50 # Invalid stock
    inventory_df.loc[1, 'LastRestockDate'] = 'Yesterday' # Ambiguous date
    inventory_df = pd.concat([inventory_df, inventory_df.iloc[[2]]]) # Duplicate


    # Save datasets
    orders_df.to_csv("orders_dirty.csv", index=False)
    with open("clickstream_dirty.json", "w") as f:
        json.dump(clickstream, f, indent=4)
    inventory_df.to_csv("inventory_dirty.csv", index=False)



    print("Sample datasets generated successfully.")