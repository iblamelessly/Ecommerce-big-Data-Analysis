import pandas as pd

base = r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\Data"

customers = pd.read_csv(base + r"\olist_customers_dataset.csv")
geolocation = pd.read_csv(base + r"\olist_geolocation_dataset.csv")
order_items = pd.read_csv(base + r"\olist_order_items_dataset.csv")
payments = pd.read_csv(base + r"\olist_order_payments_dataset.csv")
reviews = pd.read_csv(base + r"\olist_order_reviews_dataset.csv")
orders = pd.read_csv(base + r"\olist_orders_dataset.csv")
products = pd.read_csv(base + r"\olist_products_dataset.csv")
sellers = pd.read_csv(base + r"\olist_sellers_dataset.csv")
category = pd.read_csv(base + r"\product_category_name_translation.csv")

print("CUSTOMERS    :", customers.shape)
print("GEOLOCATION  :", geolocation.shape)
print("ORDER ITEMS  :", order_items.shape)
print("PAYMENTS     :", payments.shape)
print("REVIEWS      :", reviews.shape)
print("ORDERS       :", orders.shape)
print("PRODUCTS     :", products.shape)
print("SELLERS      :", sellers.shape)
print("CATEGORY     :", category.shape)