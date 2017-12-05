#performs the desired calculations for our data
import scipy.stats as st
import numpy as np
import math
from matplotlib import pyplot as plt
import matplotlib.mlab as mlab

class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #Prints the spearman and pearson correlation coeffectients
    def correlation(self):
        print(st.spearmanr(self.x,self.y))
        print(st.pearsonr(self.x, self.y))
    #Graphs the normal distributions for each mean and variance passed
    def normDist(self, mean, var):
        for mean, var in zip(mean, var):
            x1 = np.linspace(mean - 3 * math.sqrt(var), mean + 3 * math.sqrt(var), 100)
            plt.plot(x1, mlab.normpdf(x1, mean, math.sqrt(var)))
        plt.show()