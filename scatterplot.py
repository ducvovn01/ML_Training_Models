import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal (5.0, 1.0, 100000)
y = np.random.normal (10.0, 2.0, 100000)

plt.scatter (x, y)
plt.show()