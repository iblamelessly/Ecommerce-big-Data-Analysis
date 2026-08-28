import pandas as pd
import matplotlib.pyplot as plt

file = r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\output\sales_master.csv"

df = pd.read_csv(file)

state_sales = df.groupby("customer_state")["price"].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 5))
state_sales.plot(kind="bar")

plt.title("Sales by State")
plt.xlabel("State")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig(
    r"C:\Users\25127\OneDrive\Desktop\Ecommerce big Data Analysis\output\sales_by_state.png"
)
