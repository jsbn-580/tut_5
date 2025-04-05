import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stud.csv")
print(df)

df.set_index('rollno', inplace=True)
print(df)

print(df[['name', 'mark']])

sorted_by_name = df.sort_values(by='name')
print(sorted_by_name[['name', 'mark']])

sorted_by_mark = df.sort_values(by='mark', ascending=False)
print(sorted_by_mark[['name', 'mark']])

print("Average:", df['mark'].mean())
print("Median:", df['mark'].median())
print("Mode:", df['mark'].mode()[0])

print("Minimum:", df['mark'].min())
print("Maximum:", df['mark'].max())

print("Variance:", df['mark'].var())
print("Standard Deviation:", df['mark'].std())

df['mark'].plot(kind='hist')
plt.show()

df.drop(columns=['place'], inplace=True)
print(df)
