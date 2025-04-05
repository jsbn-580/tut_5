import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [21, 22, 23]
})
df.to_excel('data1.xlsx', index=False)
