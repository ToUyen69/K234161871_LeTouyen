import pandas as pd

def top3_best_selling_products(df):
    df.columns = df.columns.str.strip()
    df["Revenue"] = df["UnitPrice"] * df["Quantity"] * (1 - df["Discount"])
    product_revenue = df.groupby("ProductID")["Revenue"].sum()
    top3_products = product_revenue.sort_values(ascending=False).head(3)

    return top3_products

df = pd.read_csv("../datasets/SalesTransactions.csv")

result = top3_best_selling_products(df)
print("Top 3 sản phẩm có doanh thu lớn nhất:")
print(result)
