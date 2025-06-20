import pandas as pd
import json

# Load datasets
orders = pd.read_csv("data/sample_data/orders_sample.csv")
with open("data/sample_data/clickstream_sample.json") as f:
    clickstream = pd.DataFrame(json.load(f))
inventory = pd.read_csv("data/sample_data/inventory_sample.csv")

# Validate inventory length
print(f"Inventory records: {len(inventory)}")  # Should be 500

# Validate product categories
valid_categories = ["Electronics", "Home Appliances", "Furniture", "Clothing"]
product_category_map = {
    "TV": "Electronics", "Laptop": "Electronics", "Phone": "Electronics",
    "Fridge": "Home Appliances", "Microwave": "Home Appliances", "Washer": "Home Appliances",
    "Sofa": "Furniture", "Table": "Furniture", "Chair": "Furniture",
    "Shirt": "Clothing", "Jeans": "Clothing", "Jacket": "Clothing"
}

invalid_rows = inventory[~inventory["product_category"].isin(valid_categories)]
if not invalid_rows.empty:
    print("Inventory: Invalid categories found:\n", invalid_rows[["product_name", "product_category"]])

for _, row in inventory.iterrows():
    product_prefix = row["product_name"].split()[0]
    expected_category = product_category_map.get(product_prefix, "Unknown")
    if expected_category != row["product_category"] and expected_category != "Unknown":
        print(f"Inventory: Mismatch - {row['product_name']} should be in {expected_category}, not {row['product_category']}")

# Validate key linkages
orders_products = set(orders["product_id"])
inventory_products = set(inventory["product_id"])
clickstream_products = set(clickstream["product_id"])
print(f"Orders products in Inventory: {orders_products.issubset(inventory_products)}")
print(f"Clickstream products in Inventory: {clickstream_products.issubset(inventory_products)}")