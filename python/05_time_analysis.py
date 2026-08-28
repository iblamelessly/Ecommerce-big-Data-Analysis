import pandas as pd

file = r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\output\sales_master.csv"

sales = pd.read_csv(file)

sales["order_purchase_timestamp"] = pd.to_datetime(
    sales["order_purchase_timestamp"]
)

sales["month"] = sales["order_purchase_timestamp"].dt.to_period("M").astype(str)

monthly_sales = (
    sales.groupby("month")["price"]
    .sum()
    .reset_index()
)

print("MONTHLY SALES:")
print(monthly_sales)

monthly_sales.to_csv(
    r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\output\monthly_sales.csv",
    index=False
)

print("\nMonthly sales file saved successfully!")