import numpy as np

ages = [22,25,34,22,13,34,11,18,17,24,48,30,29,40,33,27,38,26,29,19]

#studying percentile: bách phân vị
ages_40 = np.percentile(ages, 40)

print (ages_40)