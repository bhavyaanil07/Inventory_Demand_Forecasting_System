import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# -----------------------------
# Configuration
# -----------------------------
NUM_RECORDS = 10000

products = {
    "Laptop": "Electronics",
    "Mouse": "Electronics",
    "Keyboard": "Electronics",
    "Monitor": "Electronics",
    "Phone": "Electronics",
    "Tablet": "Electronics",
    "Printer": "Electronics",
    "Headphones": "Electronics",
    "Speaker": "Electronics",
    "Camera": "Electronics",

    "Rice": "Groceries",
    "Milk": "Groceries",
    "Bread": "Groceries",
    "Eggs": "Groceries",
    "Sugar": "Groceries",
    "Tea": "Groceries",
    "Coffee": "Groceries",
    "Butter": "Groceries",
    "Cheese": "Groceries",
    "Juice": "Groceries",

    "Shampoo": "Personal Care",
    "Soap": "Personal Care",
    "Toothpaste": "Personal Care",
    "Perfume": "Personal Care",
    "Lotion": "Personal Care",
    "Face Wash": "Personal Care",
    "Hair Oil": "Personal Care",
    "Conditioner": "Personal Care",
    "Deodorant": "Personal Care",
    "Sanitizer": "Personal Care"
}

suppliers = [
    "ABC Suppliers",
    "Global Traders",
    "Prime Distribution",
    "Nova Supply",
    "Smart Wholesale"
]

start_date = datetime(2023, 1, 1)

records = []

for i in range(NUM_RECORDS):

    product = random.choice(list(products.keys()))
    category = products[product]

    date = start_date + timedelta(days=random.randint(0, 730))

    month = date.month

    # Seasonal demand
    seasonal_factor = 1

    if month in [11, 12]:
        seasonal_factor = 1.6

    elif month in [6, 7]:
        seasonal_factor = 1.3

    units_sold = max(1, int(np.random.normal(40 * seasonal_factor, 10)))

    inventory = random.randint(40, 500)

    price = round(random.uniform(10, 2000), 2)

    promotion = random.choice(["Yes", "No"])

    lead_time = random.randint(2, 15)

    supplier = random.choice(suppliers)

    revenue = round(units_sold * price, 2)

    records.append([
        date.date(),
        product,
        category,
        units_sold,
        inventory,
        price,
        promotion,
        supplier,
        lead_time,
        revenue
    ])

df = pd.DataFrame(records, columns=[
    "Date",
    "Product_Name",
    "Category",
    "Units_Sold",
    "Inventory_Level",
    "Price",
    "Promotion",
    "Supplier",
    "Lead_Time",
    "Revenue"
])

df.to_csv("data/raw/inventory_data.csv", index=False)

print("Dataset generated successfully!")
print(df.head())
print(f"\nTotal Records: {len(df)}")