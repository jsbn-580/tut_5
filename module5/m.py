import pandas as pd

df = pd.read_csv('employee.csv')
print(df.head(7))
print(df['name'].sort_values())
print(df[df['salary'] == df['salary'].max()]['name'])
print(df[df['gender'] == 'Male']['name'])
print(df['team'].unique())
