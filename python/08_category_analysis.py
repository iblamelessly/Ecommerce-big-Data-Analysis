import pandas as pd
import matplotlib.pyplot as plt

file = r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\output\sales_master.csv"

df = pd.read_csv(file)

category_sales = df.groupby("product_category_name")["price"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))

category_sales.plot(kind="bar")

plt.title("Top 10 Product Categories by Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\output\top_categories.png"
)

plt.show()