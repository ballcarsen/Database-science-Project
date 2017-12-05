import scipy.stats as st
class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def correlation(self):
        print(st.spearmanr(self.x,self.y))
        print(st.pearsonr(self.x, self.y))