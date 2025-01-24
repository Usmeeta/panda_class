import  pandas as pd

# Create a DataFrame from a dictionary
data = {
    "Product": ["Apple", "Banana", "Orange", "Grapes"],
    "Price": [350, 120, 60, 200],
    "Quantity": [10, 15, 8, 12]
    }
df = pd.DataFrame(data)
print("DataFrame:")
print(df)


# Add new column
df["Total"] = df["Price"] * df["Quantity"]
print("\nDataFrame with Total column:")
print(df)

# Save DataFrame to a CSV file
df.to_csv('product.csv', index=False)
print("\nData saved to product.csv")