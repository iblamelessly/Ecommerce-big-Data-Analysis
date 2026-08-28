import pandas as pd

file = r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\output\sales_master.csv"

sales = pd.read_csv(file)

# Basic calculations
total_sales = sales["price"].sum()
total_orders = sales["order_id"].nunique()
total_customers = sales["customer_unique_id"].nunique()
average_order_value = total_sales / total_orders

print("TOTAL SALES: ₹", round(total_sales, 2))
print("TOTAL ORDERS:", total_orders)
print("TOTAL CUSTOMERS:", total_customers)
print("AVERAGE ORDER VALUE: ₹", round(average_order_value, 2))

# Top 10 categories
top_categories = sales.groupby("product_category_name")["price"].sum().sort_values(ascending=False).head(10)

print("\nTOP 10 CATEGORIES BY SALES:")
print(top_categories)