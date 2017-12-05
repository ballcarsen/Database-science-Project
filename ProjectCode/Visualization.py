import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
class Vis():
    def __init__(self, x, y, xlabel = 'Null', ylabel = 'Null', title = 'Null'):
        self.x = x
        self.y = y
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
    def plot(self, size = (np.pi*3)):
        self.x = np.array(self.x)
        self.y = np.array(self.y)
        colors = (0, 0, 0)
        slope, intercept, r_value, p_value, std_err = st.linregress(self.x, self.y)
        plt.scatter(self.x, self.y, s=size, c=colors, alpha=0.5)
        plt.plot(self.x, intercept + self.x * slope)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.show()