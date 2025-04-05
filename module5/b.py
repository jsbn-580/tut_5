import pandas as pd

data = [['Alice', 21], ['Bob', 22], ['Charlie', 23]]
df = pd.DataFrame(data, columns=['Name', 'Age'], index=['s1', 's2', 's3'])
print(df)
