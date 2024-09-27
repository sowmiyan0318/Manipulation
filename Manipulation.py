import pandas as pd
import numpy as np

# Create a sample dataset
data = {
    'name': ['John', 'Mary', 'Jane', 'Bob', 'Alice', 'John'],
    'age': [25, 31, 22, 35, 28, 25],
    'score': [90, 80, 95, 75, 85, 90],
    'date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-01-01']
}

df = pd.DataFrame(data)

# View the first few rows of the data
print(df.head())

# Check for duplicate rows
print(df.duplicated().sum())

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Extract the year from the 'date' column
df['year'] = df['date'].dt.year

# Group the data by 'year' and calculate the mean of 'score'
grouped_df = df.groupby('year')['score'].mean()

# Print the result
print(grouped_df)

# Sort the data by 'score' in descending order
df_sorted = df.sort_values('score', ascending=False)

# Print the sorted data
print(df_sorted.head())
