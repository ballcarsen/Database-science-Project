import numpy as np
import math
from matplotlib import pyplot as plt
import matplotlib.mlab as mlab

def normDist(mean, var):
    for mean,var in zip(mean,var):
        x1 = np.linspace(mean - 3 * math.sqrt(var), mean + 3 * math.sqrt(var), 100)
        plt.plot(x1, mlab.normpdf(x1, mean, math.sqrt(var)))
    plt.show()