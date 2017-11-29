import scipy.stats as st
class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def spearmans(self):
        print(st.spearmanr(self.x,self.y))