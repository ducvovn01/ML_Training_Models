import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('house_data.csv')

X = df[['Area', 'Bed', 'Age']]
y = df['Price']

model = LinearRegression()
model.fit(X, y)
r = model.predict ([[100, 3, 10]])
print (r)
print (model.coef_)