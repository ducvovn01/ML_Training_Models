import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import sklearn.datasets as fetch_california_housing


#Loading dataset
df = fetch_california_housing(as_frame = True)
X = df.data
y = df.target

#Splitting dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

#Standardizing the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model1 = Ridge(alpha = 0.5)
model1.fit(X_train_scaled, y_train)

y_pred = model1.predict(X_test_scaled)
print("Ridge coefficients: ", model1.coef_)
print("Ridge intercept: ", model1.intercept_)
print("Ridge predictions: ", y_pred)


