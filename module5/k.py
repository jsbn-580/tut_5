import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales.csv')

plt.scatter(df['month_number'], df['toothpaste'], color='blue', label='Toothpaste Sales')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.title('Toothpaste Sales Data per Month')
plt.grid(True)
plt.legend()
plt.show()

plt.bar(df['month_number'] - 0.2, df['facecream'], width=0.4, label='Face Cream', color='orange')
plt.bar(df['month_number'] + 0.2, df['facewash'], width=0.4, label='Face Wash', color='green')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.title('Face Cream and Face Wash Sales Data')
plt.legend()
plt.show()

total_sales = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('Total Product Sales for the Year')
plt.axis('equal')
plt.show()
