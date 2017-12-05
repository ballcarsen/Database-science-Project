#Script for question 3
#imports
import csv
from ProjectCode.network import  Network
import ProjectCode.statistics as stat
from ProjectCode.Visualization import Vis
import ProjectCode.Calculations as calc
import numpy as np
#data file
file = 'question3.csv'

def run():
    #array of the data
    data = []
    #post process the query
    with open(file, 'rb') as Data:
        read = csv.reader(Data)
        for i in Data:
            i = i.split()
            if len(i) == 3:
                for k in range(len(i)):
                    temp = str(i[k])
                    temp =  temp.replace("b", "")
                    temp = temp.replace("\'", "")
                    i[k] = temp
                data.append(i)
    #data arrays for the nueral networks
    fan = []
    critic = []
    rev = []
    #Data arrays for visualisation, needs a slightly different format
    fanVis = []
    criticVis = []
    revVis = []

    #Parse through the data set
    for i in range(len(data)):
        fanVis.append(float(data[i][0]))
        criticVis.append(float(data[i][1]))
        revVis.append(float(data[i][2]))
        fan.append([float(data[i][0])])
        critic.append([float(data[i][1])])
        rev.append(float(data[i][2]))

    #Plots fan ratings vs revenue and critic ratings vs revenue
    v1 = Vis(fanVis,revVis, 'Rating', 'Revenue', 'Fan Rating VS Revenue')
    v2 = Vis(criticVis, revVis, 'Rating', 'Revenue', 'Critic Rating VS Revenue')
    v1.plot()
    v2.plot()
    #Nueral network parameters, number of nodes in the hidden layers and learning rate
    params = [[20, .5], [100, .5], [1000, .5], [20, .05], [100, .05], [1000, .05], [20, .005], [100, .005], [1000, .5], [1000, .05], [1000, .005]]
    #Results from a certain set of parameters
    results = []
    #Results from all the sets of parameters
    doubleResults = []
    #Mean and variance from the neural networks trained on fan
    fanMean = []
    fanVar = []
    #Test train 11 different neural nets, 30 times for fan reviews
    for i in range(len(params)):
        for k in range(30):
            net = Network(fan,rev, params[i][1], 1)
            net.preProcess()
            results.append(net.backProp(params[i][0]))
        fanMean.append(np.mean(results))
        fanVar.append(np.var(results))
        doubleResults.append(results)
        results = []

    res = np.array(doubleResults)
    #Saves results as a txt file
    np.savetxt('fanResults.txt', res, fmt='%1.3f')
    #Graphs normal distributions of the results from the networks for fan reviews
    calc.normDist(fanMean, fanVar)

    #Mean error for the nueral networks trained on critic reviews
    criticMean = []
    criticVar = []
    doubleResults = []
    results = []
    #Test train 11 different neural nets, 30 times for critic reviews

    for i in range(len(params)):
        for k in range(30):
            net = Network(critic,rev, params[i][1], 1)
            net.preProcess()
            results.append(float(net.backProp(params[i][0])))
        criticMean.append(np.mean(results))
        criticVar.append(np.var(results))
        doubleResults.append(results)
        results = []

    #saves the results from the networks for critic reviews
    res = np.array(doubleResults)
    np.savetxt('criticResults.txt', res, fmt='%1.3f')
    #Graphs normal distributions of the results from the networks for critic reviews
    calc.normDist(criticMean, criticVar)

    print(fanMean)
    print(criticMean)
