import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
class Vis():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def plot(self):
        self.x = np.array(self.x)
        self.y = np.array(self.y)
        colors = (0, 0, 0)
        area = np.pi * 3
        slope, intercept, r_value, p_value, std_err = st.linregress(self.x, self.y)
        plt.scatter(self.x, self.y, s=area, c=colors, alpha=0.5)
        plt.plot(self.x, intercept + self.x * slope)
        plt.show()