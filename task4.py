import pandas as pd
import numpy as np

data1 = {
    "Costumer_id": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"],
}
data2 = {
    "Order_id": [101, 102, 103, 104, 105],
    "Costumer_id": [3, 4, 5, None, 6],
    "Amount": [25000, 30000, 35000, 40000, np.nan]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge DataFrames with an outer join to retain all rows
merged_df = pd.merge(df1, df2, on="Costumer_id", how="outer")
print("Merged DataFrame (Outer Join):")
print(merged_df)


# Drop rows with missing values
# merged_df = merged_df.dropna()
# print("\nDataFrame after dropping rows with missing values:")
# print(merged_df)

# Fill missing values with a specific value
if "Amount" in merged_df.columns:
    merged_df["Amount"] = merged_df["Amount"].fillna(merged_df["Amount"].mean())
if "Order_id" in merged_df.columns:
    merged_df["Order_id"] = merged_df["Order_id"].fillna("unknown")
if "Costumer_id" in merged_df.columns:
    merged_df["Costumer_id"] = merged_df["Costumer_id"].fillna("Unknown")
if "Name" in merged_df.columns:
    merged_df["Name"] = merged_df["Name"].fillna("Unknown")
print("\nDataFrame after filling missing values:")
print(merged_df)

# Sort by Amount in descending order
sorted_df = merged_df.sort_values(by="Amount", ascending=False)
print("\nDataFrame sorted by Amount:")
print(sorted_df)

# Save DataFrame to a CSV file
sorted_df.to_csv('task4.csv', index=False)
print("\nData saved to task4.csv")
