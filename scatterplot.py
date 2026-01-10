import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

x = np.random.normal (5.0, 1.0, 100000)
y = np.random.normal (10.0, 2.0, 100000)


slope, intercept, r, p, std_err = stats.lingress(x, y)

def lingress(x, slope, intercept):
    return slope*x + intercept
plt.scatter (x, y)
plt.plot(x, lingress(x, slope, intercept))
plt.show()