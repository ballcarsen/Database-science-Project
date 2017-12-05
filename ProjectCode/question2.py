#Script for question 2
#Imports
import numpy as np
from ProjectCode.Visualization import Vis
from ProjectCode.Calculations import Calc
import csv
from ProjectCode.network import Network
#data file
file = "question2.csv"

def run():
    #input values
    x = []
    #output values
    y = []
    #Post Process Query
    with open(file, 'rb') as Data:
        read = csv.reader(Data)

        for i in Data:

            i = i.split()
            if len(i) == 5:
                for k in range(len(i)):
                    if k != 4:
                        temp = str(i[k])
                        temp =  temp.replace("b", "")
                        temp = temp.replace("\'", "")
                        i[k] = float(temp)
                    else:
                        temp = str(i[k])
                        temp =  temp.replace("b", "")
                        temp = temp.replace("\'", "")
                        y.append(float(temp))
                i.pop()
                x.append(i)
    Data.close()
    x = np.array(x)
    y = np.array(y)
    #Parameters for the nerural network, number of nodes in a hidden layer and learning rate
    params = [[20, .5], [100, .5], [1000, .5], [20, .05], [100, .05], [1000, .05], [20, .005], [100, .005], [1000, .5], [1000, .05], [1000, .005]]
    #Results from an individual train/test
    results = []
    #results from all the train/test runs
    doubleResults = []
    #average facebook likes
    avg = []
    #number of faces in the poster
    face = []
    #Iterate through the data set
    for i in range(len(x)):

        face.append(x[i][3] * 5)
        #averages the facebook likes of the people from the production
        avg.append(float(x[i][0]) + float(x[i][1]) + float(x[i][2]) / 3)
    #Correlation between the average facebook likes and revenue
    C1 = Calc(avg, y)
    C1.correlation()
    #Plots the average facebook likes with the size of the data point as number of faces in the poster
    v1 = Vis(avg, y, 'Avg Crew FB Likes', 'Revenue', 'Facebook likes of Crew vs Revenue')
    v1.plot(face)
    #mean and variance from the results of training on a certain set of parameters
    mean = []
    var = []

    #Trains and tests 11 different neural networks, 30 times
    for i in range(len(params)):
        for k in range(30):
            net = Network(x,y, params[i][1], 10000)
            net.preProcess()
            results.append(net.backProp(params[i][0]))
        mean.append(np.mean(results))
        var.append(np.var(results))
        doubleResults.append(results)
        results = []
    #outputs the results from train/tests
    res = np.array(doubleResults)
    np.savetxt('q2Results.txt', res, fmt='%1.3f')
    #Graphs the normal distributions for the 11 different neural networks for 30 test/trains
    C1.normDist(mean,var)