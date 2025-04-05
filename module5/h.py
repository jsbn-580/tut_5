import pandas as pd

df = pd.read_csv("auto.csv")
df.dropna(inplace=True)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
df.dropna(inplace=True)

most_expensive_company = df[df['price'] == df['price'].max()]['company']
print(most_expensive_company)

toyota_cars = df[df['company'].str.lower() == 'toyota']
print(toyota_cars)

total_cars = df['company'].value_counts()
print(total_cars)

highest_priced = df.groupby('company')['price'].max()
print(highest_priced)

avg_mileage = df.groupby('company')['average-mileage'].mean()
print(avg_mileage)

sorted_df = df.sort_values(by='price', ascending=False)
print(sorted_df)
