import pandas as pd
import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Create a DataFrame from a dictionary
data = {
    "Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05"],
    "Temperature": [25, 28, 22, 26, 24],
    "Humidity": [60, 55, 70, 65, 75]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Plot the temperature over date
df.plot(x="Date", y="Temperature", kind="line", marker="o")
plt.savefig('temperature.png')
plt.show()

# Save DataFrame to a CSV file
df.to_csv('climate.csv', index=False)
print("\nData saved to climate.csv")
