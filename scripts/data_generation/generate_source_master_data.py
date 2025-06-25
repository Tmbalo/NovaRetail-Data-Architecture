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

            "Gender": [random.choice(["Male", "Female", "Other"]) for _ in range(n)],

            "Phone": [fake.phone_number() for _ in range(n)],

            "SignupDate": [fake.date_between(start_date='-2y', end_date='-1d') for _ in range(n)],
            
            "Region": [random.choice(["US", "EU", "APAC", "UK", "CA"]) for _ in range(n)],
            
            "LoyaltyPoints": [random.randint(0, 1000) for _ in range(n)],
            
            "AccountStatus": [random.choice(["Active", "Inactive", "Suspended"]) for _ in range(n)],
            
            "LastLogin": [fake.date_time_between(start_date='-1y', end_date='now') for _ in range(n)],
            
            "PreferredLanguage": [random.choice(["English", "Spanish", "French", "German", "Chinese"]) for _ in range(n)],
            
            "PreferredPaymentMethod": [random.choice(["Credit Card", "PayPal", "Bank Transfer"]) for _ in range(n)],
            
            "LastPurchaseDate": [fake.date_time_between(start_date='-1y', end_date='now') for _ in range(n)],
            
            "Address": [fake.address().replace("\n", ", ") for _ in range(n)]
            
          

        })







def generate_products(n=50):
    category_templates = {
        "Electronics": [
            lambda: f"{fake.word().capitalize()} Headphones",
            lambda: f"{fake.word().capitalize()} Smartphone",
            lambda: f"{fake.word().capitalize()} Laptop",
            lambda: f"{fake.word().capitalize()} Camera"
        ],
        "Books": [
            lambda: f"{fake.word().capitalize()} Tales",
            lambda: f"The Art of {fake.word().capitalize()}",
            lambda: f"{fake.word().capitalize()} Guide",
            lambda: f"{fake.word().capitalize()} Stories"
        ],
        "Clothing": [
            lambda: f"{fake.color_name()} T-Shirt",
            lambda: f"{fake.color_name()} Jeans",
            lambda: f"{fake.color_name()} Jacket",
            lambda: f"{fake.color_name()} Dress"
        ],
        "Home": [
            lambda: f"{fake.word().capitalize()} Lamp",
            lambda: f"{fake.word().capitalize()} Sofa",
            lambda: f"{fake.word().capitalize()} Table",
            lambda: f"{fake.word().capitalize()} Chair"
        ],
        "Toys": [
            lambda: f"{fake.word().capitalize()} Puzzle",
            lambda: f"{fake.word().capitalize()} Doll",
            lambda: f"{fake.word().capitalize()} Car",
            lambda: f"{fake.word().capitalize()} Blocks"
        ]
    }

    categories = []
    product_names = []
    for _ in range(n):
        category = random.choice(list(category_templates.keys()))
        name = random.choice(category_templates[category])()
        categories.append(category)
        product_names.append(name)

    return pd.DataFrame({
        "ProductID": [f"P{i+1:04d}" for i in range(n)],
        "ProductName": product_names,
        "Category": categories,
        "Price": [round(random.uniform(10, 500), 2) for _ in range(n)],
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