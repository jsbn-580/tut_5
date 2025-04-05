import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather.csv')
print(df.head(10))

print("Maximum temperature:", df['temperature'].max())
print("Minimum temperature:", df['temperature'].min())

print("Places with temperature < 28°C:\n", df[df['temperature'] < 28]['place'])

print("Places with 'Cloudy' weather:\n", df[df['weather'] == 'Cloudy']['place'])

print("Weather frequency:\n", df['weather'].value_counts().sort_index())

plt.figure(figsize=(10, 5))
plt.bar(df['date'], df['temperature'], color='skyblue')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature of Each Day')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
