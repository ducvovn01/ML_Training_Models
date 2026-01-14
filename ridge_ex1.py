import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
import pandas as pd

np.random.seed(1)
n_samples = 50
age = np.random.randint(20, 60, (n_samples, 1))
salary = np.random.randint(10000000, 50000000, (n_samples, 1))

X = np.hstack((age, salary))

y = 2 * age.flatten() + 0.000005 * salary.flatten() + np.random.randn(n_samples)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = Ridge(alpha=1.0)
model.fit(X_scaled, y)

y1 = model.predict(X_scaled)
print(y1)
print (model.coef_)
print (model.intercept_)