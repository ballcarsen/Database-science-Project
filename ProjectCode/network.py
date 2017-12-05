from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor as bpNet
from sklearn.model_selection import train_test_split
import numpy as np
#A nueral network
class Network:
    #accepts the input data, x, the expected output, y, the learning rate and the maximum number of iterations
    def __init__(self, x, y, learningRate, maxIter):
        self.learningRate = learningRate
        self.x = x
        self.y = y
        self.in_train = np.array([])
        self.in_test = np.array([])
        self.out_train = np.array([])
        self.out_test = np.array([])
        self.maxIter = maxIter
        self.testsSplit = []
        self.trainSplit = []
    #Trains and test a MLP, given hiddenLayer size. It returns the mean error produced by the test set
    def backProp(self, hiddenLayerSize):
        net = bpNet(alpha = self.learningRate , hidden_layer_sizes = hiddenLayerSize, max_iter= self.maxIter,
                    activation = 'logistic', verbose = 'True', learning_rate = 'adaptive')
        net.fit(self.in_train, self.out_train)
        test_result = net.predict(self.in_test)
        return(np.math.sqrt(mean_squared_error(self.out_test, test_result)))

    #Create a train and test set
    def preProcess(self):
        self.in_train, self.in_test, self.out_train, self.out_test = train_test_split(self.x, self.y)
