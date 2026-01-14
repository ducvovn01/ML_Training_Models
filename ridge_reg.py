import pandas as pd
from sklearn.linear_model import Ridge, LinearRegression

df = pd.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

model1 = LinearRegression()
model2 = Ridge(alpha = 1.0)
model1.fit(X, y)
model2.fit(X, y)

print("Ridge intercept: ", model2.intercept_)
print("Ridge coefficients: ", model2.coef_)

print ("Linear intercept:", model1.intercept_)
print("Linear coefficients:", model1.coef_)
y_pre = model2.predict([[1300, 3.0]])
y_pre1 = model1.predict([[1300, 3.0]])
print("Ridge predictions: ", y_pre)
print("Linear predictions: ", y_pre1)
