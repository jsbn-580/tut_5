import pandas as pd

df = pd.DataFrame({
    'Product': ['A', 'B', 'C'],
    'Price': [100, 200, 300]
})
df.to_excel('data2.xlsx', index=False)
