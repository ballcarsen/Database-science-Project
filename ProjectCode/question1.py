#imports
import csv
from ProjectCode import Visualization
from ProjectCode import Calculations

#data file
file = "question1.csv"

def run():
    #Array of the data
    data = []
    #Reads data
    with open(file, 'rb') as Data:
        read = csv.reader(Data)

        for i in Data:
            rating = 0
            budget = 0
            i = i.split()
            if len(i) == 7:
                for k in range(len(i)):
                    temp = str(i[k])
                    temp =  temp.replace("b", "")
                    temp = temp.replace("\'", "")
                    i[k] = temp
                data.append(i)
    Data.close()
    #Budget and a directors average production rating
    Budget = []
    directorPopularity= []
    #Will hold the current film that we are calculating the directors avg production rating for all of their movies
    compare = data[0][4]
    #Budget of the current film
    budget = 0
    #sum of the ratings for the directors films
    rating = 0
    count = 0
    #Parses through the data set, calculating the average rating of the films each director has produced
    for i in data:
        id = i[4]
        if id == compare:
            budget = float(i[0])
            rating += float(i[6])
            count += 1
        else:
            if count == 0:
                count = 1
            if rating > 0 and budget < 500000000:
                Budget.append(float(budget))
                directorPopularity.append(float(rating / count))

            rating = 0
            count = 0
            compare = id
    #Plots the budget of each film vs the average rating of the directors films
    vis1 = Visualization.Vis(Budget, directorPopularity, 'Budget', 'Average Rating of Films by Director', 'Budget in Correlation to the Average Rating of Films by the Driector')
    vis1.plot()
    #Calculates the correleation coeffection of the budget of each film vs the average rating of the directors films
    calc = Calculations.Calc(Budget, directorPopularity)
    calc.correlation()

