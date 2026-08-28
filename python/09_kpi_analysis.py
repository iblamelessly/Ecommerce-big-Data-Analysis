import pandas as pd

file = r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\output\sales_master.csv"

df = pd.read_csv(file)

total_sales = df["price"].sum()
total_orders = df["order_id"].nunique()
total_customers = df["customer_unique_id"].nunique()
average_order_value = total_sales / total_orders

kpi = pd.DataFrame({
    "KPI": [
        "Total Sales",
        "Total Orders",
        "Total Customers",
        "Average Order Value"
    ],
    "Value": [
        total_sales,
        total_orders,
        total_customers,
        average_order_value
    ]
})

print(kpi)

kpi.to_csv(
    r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\output\kpi.csv",
    index=False
)

print("\nKPI file saved successfully!")