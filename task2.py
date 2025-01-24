import pandas as pd

data = {
    "Student": ["Alice", "Alice", "Charlie", "Charlie", "Bob", "Bob"],
    "Subject": ["Math", "Science", "Math", "Science", "Math", "Science"],
    "Score": [85, 90, 75, 80, 95, 88]
}

df = pd.DataFrame(data)

# Group by department and calculate average salary
avg_score = df.groupby("Student")["Score"].mean()
print("Average Score by Student:")
print(avg_score)

# Filter rows where Score > 85
filtered_df = df[df['Score'] > 85]
print("\nFiltered DataFrame:")
print(filtered_df)