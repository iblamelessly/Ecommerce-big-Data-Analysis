import pandas as pd

base = r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\Data"

orders = pd.read_csv(base + r"\olist_orders_dataset.csv")
items = pd.read_csv(base + r"\olist_order_items_dataset.csv")
customers = pd.read_csv(base + r"\olist_customers_dataset.csv")
payments = pd.read_csv(base + r"\olist_order_payments_dataset.csv")
products = pd.read_csv(base + r"\olist_products_dataset.csv")

print("ORDERS")
print(orders.head())
print("\nColumns:", orders.columns.tolist())

print("\nORDER ITEMS")
print(items.head())
print("\nColumns:", items.columns.tolist())

print("\nCUSTOMERS")
print(customers.head())
print("\nColumns:", customers.columns.tolist())

print("\nPAYMENTS")
print(payments.head())
print("\nColumns:", payments.columns.tolist())

print("\nPRODUCTS")
print(products.head())
print("\nColumns:", products.columns.tolist())