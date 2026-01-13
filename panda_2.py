#We will learn about file importing in pandas

import pandas as pd

df = pd.read_csv('data.csv')
X = df[['Model', 'Volume']]
y = df['CO2']

print(X)
print(y)