import pandas as pd
import matplotlib.pyplot as plt

file = r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\output\monthly_sales.csv"

df = pd.read_csv(file)

plt.figure(figsize=(12, 5))
plt.plot(df["month"], df["price"], marker="o")
plt.title("Monthly E-Commerce Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\output\monthly_sales.png"
)

plt.show()