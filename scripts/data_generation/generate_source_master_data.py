import pandas as pd
import random
from faker import Faker
from datetime import datetime
import json

# Initialize Faker
fake = Faker()
Faker.seed(456)
random.seed(456)
# Create Customer and Product datasets
def generate_customers(n=100):
        return pd.DataFrame({
            "CustomerID": [f"C{i+1:05d}" for i in range(n)],
            "CustomerName": [fake.name() for _ in range(n)],
            "Email": [fake.email() for _ in range(n)],
            "Phone": [fake.phone_number() for _ in range(n)],
            "SignupDate": [fake.date_between(start_date='-2y', end_date='-1d') for _ in range(n)]
        })


def generate_products(n=50):
        return pd.DataFrame({
            "ProductID": [f"P{i+1:04d}" for i in range(n)],
            "ProductName": [fake.word().capitalize() + " " + fake.color_name() for _ in range(n)],
            "Category": [random.choice(["Electronics", "Books", "Clothing", "Home", "Toys"]) for _ in range(n)],
            "Price": [round(random.uniform(10, 500), 2) for _ in range(n)]
        })




# Main execution
if __name__ == "__main__":
    customers_df = generate_customers()
    # Inject missing and inconsistent data into customers
    customers_df.loc[0, 'Email'] = None # Missing email
    customers_df.loc[1, 'Phone'] = '000-123' # Invalid phone format
    customers_df.loc[2, 'CustomerName'] = customers_df.loc[2, 'CustomerName'].lower() # Inconsistent case
    customers_df = pd.concat([customers_df, customers_df.iloc[[3]]]) # Duplicate row
    
    products_df = generate_products()
    # Inject price outlier and category typo
    products_df.loc[0, 'Price'] = -99.99 # Negative price
    products_df.loc[1, 'Category'] = 'Elec-tronics' # Typo
    products_df.loc[2, 'ProductName'] = '' # Empty product name

    customers_df.to_csv("data/sample_data/customers_dirty.csv", index=False)
    products_df.to_csv("data/sample_data/products_dirty.csv", index=False)

    print("Sample Master datasets generated successfully.")
