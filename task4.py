import pandas as pd

data1 = {
    "Costumer_id": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
}
data2 = {
    "Order_id": [101, 102, 103],
    "Costumer_id": [2, 3, 4, None],
    "Amount": [25000, 30000, 35000, 40000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge DataFrames based on a common column (ID)
merged_df = pd.merge(df1, df2, on="Costumer_id", how="inner")
print("Merged DataFrame:")
print(merged_df)

# Drop rows with missing values
df = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df) 