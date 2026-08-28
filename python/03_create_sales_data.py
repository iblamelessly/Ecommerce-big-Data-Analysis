import pandas as pd

base = r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\Data"

# Load datasets
customers = pd.read_csv(base + r"\olist_customers_dataset.csv")
orders = pd.read_csv(base + r"\olist_orders_dataset.csv")
items = pd.read_csv(base + r"\olist_order_items_dataset.csv")
products = pd.read_csv(base + r"\olist_products_dataset.csv")

# Join customers with orders
sales = orders.merge(customers, on="customer_id", how="left")

# Join order items
sales = sales.merge(items, on="order_id", how="left")

# Join products
sales = sales.merge(products, on="product_id", how="left")

print("Total Rows:", len(sales))
print("Total Columns:", len(sales.columns))

print("\nColumns:")
print(sales.columns.tolist())

# Save
output = r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\output\sales_master.csv"

sales.to_csv(output, index=False)

print("\nMaster sales dataset saved successfully!")