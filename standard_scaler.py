import pandas as pd
from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([
    [1, 100000],
    [2, 500000],
    [3, 1000000],
    [4, 2000000],
    [5, 3000000]
])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

print (scaled_data)



