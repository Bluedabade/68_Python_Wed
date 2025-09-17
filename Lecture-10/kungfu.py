import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Calculate the average age
average_age = df['Age'].mean()
print("\nAverage Age:", average_age)

# Filter rows where Age is greater than 28
filtered_df = df[df['Age'] > 28]
print("\nFiltered DataFrame (Age > 28):\n", filtered_df)

# Add a new column for salary
df['Salary'] = [50000, 60000, 70000]
print("\nDataFrame with Salary column:\n", df)
