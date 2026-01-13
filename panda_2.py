import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data.csv')

X = df[['Weight', 'Volume']]
y = df['CO2']

model1 = LinearRegression()
model1.fit(X, y)

r1 = model1.predict([[2300, 1300]])
print (r1)
print (model1.coef_)