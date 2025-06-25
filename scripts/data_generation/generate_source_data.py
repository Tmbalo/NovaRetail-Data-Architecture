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
customersid_df = pd.read_csv("data/sample_data/customers_dirty.csv")
customer_ids = customersid_df['CustomerID'].dropna().tolist()

# Load products data to link orders(ProductID)
#productid_df = pd.read_csv("data/sample_data/products_dirty.csv")
#product_ids = productid_df['ProductID'].dropna().tolist()

# Load products data to link orders(ProductID)
productid_df = pd.read_csv("data/sample_data/products_dirty.csv")
product_ids = productid_df['ProductID'].dropna().tolist()
product_price_map = dict(zip(productid_df['ProductID'], productid_df['Price']))  # <-- Add this line


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
        price = product_price_map.get(product_id, 0)  # <-- Get price for product_id
        total = price * quantity
        order_date = fake.date_time_between(start_date='-3M', end_date='now')
        data.append({
            "OrderID": f"O{i+1:05d}",
            "CustomerID": customer_id,
            "ProductID": product_id,
            "Quantity": quantity,
            "TotalAmount": total,  # <-- Use calculated total
            "OrderDate": order_date.strftime("%Y-%m-%d %H:%M:%S"),
            "region": [random.choice(["US", "EU", "APAC", "UK", "CA"]) for _ in range(n)][i],
            "PaymentMethod": random.choice(["Credit Card", "PayPal", "Bank Transfer"]),
            "OrderStatus": random.choice(["Completed", "Pending", "Cancelled"]),
            "ShippingAddress": fake.address().replace("\n", ", "),
            "BillingAddress": fake.address().replace("\n", ", "),
            "Discount": round(random.uniform(0, 50), 2),  # Random discount,
            "Tax": round(total * random.uniform(0.05, 0.15), 2),  # Random tax between 5% and 15%,
            "ShippingCost": round(random.uniform(5, 20), 2),  # Random shipping cost,
            "TrackingNumber": fake.uuid4(),
            "DeliveryDate": (order_date + pd.Timedelta(days=random.randint(1, 10))).strftime("%Y-%m-%d %H:%M:%S"),
            "ReturnStatus": random.choice(["Not Returned", "Returned", "Refunded"]),
            "ReturnReason": random.choice(["Damaged", "Wrong Item", "No Longer Needed", "Other"]),
            "Rating": random.randint(1, 5),  # Random rating between 1 and 5,     
            "Review": fake.sentence(nb_words=10)  # Random review text
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
        "session_duration_seconds": random.randint(60, 600),  # Duration in seconds
        "referrer": random.choice(["Google", "Facebook", "Direct", "Email", "Other"]),
        "device_type": random.choice(["Desktop", "Mobile", "Tablet"]),  
        "browser": random.choice(["Chrome", "Firefox", "Safari", "Edge", "Internet Explorer"]),
        "location": fake.city(),
        "ip_address": fake.ipv4(),
        "search_query": fake.sentence(nb_words=3) if random.random() < 0.5 else None,  # 50% chance of having a search query
        "cart_value": round(random.uniform(0, 1000), 2) if random.random() < 0.5 else None,  # 50% chance of having a cart value
        "payment_method": random.choice(["Credit Card", "PayPal", "Bank Transfer"]),
        "order_id": f"O{random.randint(1, 500):05d}" if random.random() < 0.3 else None,  # 30% chance of having an order ID
        "transaction_amount": round(random.uniform(10, 500), 2) if random.random() < 0.3 else None,  # 30% chance of having a transaction amount
        "coupon_code": fake.bothify(text='COUPON-???-###') if random.random() < 0.2 else None,  # 20% chance of having a coupon code
        "loyalty_points_used": random.randint(0, 100) if random.random() < 0.2 else None,  # 20% chance of using loyalty points
        "feedback": fake.sentence(nb_words=5) if random.random() < 0.1 else None,  # 10% chance of having feedback
        "browser_language": random.choice(["en-US", "fr-FR", "es-ES", "de-DE", "zh-CN"]) if random.random() < 0.5 else None  # 50% chance of having a browser language
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
            "LastRestockDate": fake.date_between(start_date="-6M", end_date="-7d"), #.strftime("%Y-%m-%d"),
            "Supplier": fake.company(),
            "WarehouseLocation": fake.city(),
            "LeadTimeDays": random.randint(1, 30),
            "ExpirationDate": fake.date_between(start_date="-1M", end_date="now"), #.strftime("%Y-%m-%d"),
            "BatchNumber": fake.bothify(text='B###-???'),   
            "QualityCheckStatus": random.choice(["Passed", "Failed"]),
            "QualityCheckDate": fake.date_between(start_date="-1M", end_date="now"), #.strftime("%Y-%m-%d"),
            "LastUpdated": fake.date_time_between(start_date="-1M", end_date="now").strftime("%Y-%m-%d %H:%M:%S"),
            "SupplierContact": fake.phone_number(), 
            "SupplierEmail": fake.email(),
            "WarehouseManager": fake.name(),
            "WarehouseCapacity": random.randint(1000, 5000),
            "StockValue": round(row["Price"] * random.randint(0, 300), 2)  # Stock value based on price and stock level  
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
    orders_df.to_csv("data/sample_data/orders_dirty.csv", index=False)
    with open("data/sample_data/clickstream_dirty.json", "w") as f:
        json.dump(clickstream, f, indent=4)
    inventory_df.to_csv("data/sample_data/inventory_dirty.csv", index=False)



    print(" Sample datasets generated successfully. ")