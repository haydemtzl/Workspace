import sys
import numpy as np
import scipy.stats as stats
from scipy.stats import variation
import pylab as pl
from numpy import genfromtxt

if len(sys.argv) >= 2:
    csv_file = sys.argv[1]
    my_data = genfromtxt(csv_file, delimiter=',')
else:
    print("Please provide the csv file with the data")
    sys.exit(-1)
print("Standard Deviation: %f" % np.std(my_data))
print("Mean: %f" % np.mean(my_data))
print("Coefficient of variation: %f" % variation(my_data))
h = sorted(my_data)
fit = stats.norm.pdf(h, np.mean(h), np.std(h))
pl.plot(h,fit,'-o')
pl.hist(h,normed=True)
pl.show()
