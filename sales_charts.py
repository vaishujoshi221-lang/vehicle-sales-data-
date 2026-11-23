import pandas as pd
df = pd.read_excel("Vehicles Sales Data.xlsx")
print(df.head())
print(df.columns)

print("\n Missing Values:")
print(df.isnull().sum())

print("\n Duplicate Rows:")
print(df.duplicated().sum())
df = df.drop_duplicates()

df.columns = df.columns.str.strip()

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].apply(
        lambda x: x.strip() if isinstance(x, str) else x
    )

print("\n After Cleaning:")
print("Missing Values:")
print(df.isnull().sum())

print("Duplicate Rows:", df.duplicated().sum())
df.to_excel("Vehicles_Sales_Cleaned.xlsx", index=False)
print("Cleaned file saved successfully!")

import matplotlib.pyplot as plt
import seaborn as sns

df["SALES"] = df["QUANTITYORDERED"] * df["PRICEEACH"]
sales = df.groupby("PRODUCTLINE")["SALES"].sum()

plt.figure(figsize=(10, 5))
plt.bar(sales.index, sales.values)
plt.title("Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="STATUS")
plt.title("Vehicle Order Status")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

yearly_sales = df.groupby("YEAR_ID")["SALES"].sum()
plt.figure(figsize=(8, 5))
plt.plot(yearly_sales.index, yearly_sales.values, marker="o")
plt.title("Yearly Sales Trend")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="PRICEEACH", bins=20, kde=True)
plt.title("Product Price Distribution")
plt.xlabel("Price Each")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="QUANTITYORDERED",
    y="PRICEEACH"
)
plt.title("Quantity vs Price")
plt.xlabel("Quantity Ordered")
plt.ylabel("Price Each")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
deal_sales=df.groupby("DEALSIZE")["SALES"].sum()
plt.pie(deal_sales, labels=deal_sales.index, autopct="%1.1f%%")
plt.title("Sales by Deal Size")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.pie(sales, labels=sales.index, autopct="%1.1f%%",wedgeprops={"width": 0.4})
plt.title("Sales by Product Line")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
country_sales = df.groupby("COUNTRY")["SALES"].sum().reset_index()
sns.barplot(
    data=country_sales,
    x="COUNTRY",
    y="SALES"
)
plt.title("Sales by Country")
plt.xlabel("Country")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()






