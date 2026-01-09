import numpy as np
import scipy.stats as stats

speed = [10,20,30,40,50,60,70,80,90,100]

spe_mean = np.mean(speed)
spe_median = np.median(speed)
spe_mode = stats.mode(speed)
print (spe_mean)
print (spe_median)
print (spe_mode)