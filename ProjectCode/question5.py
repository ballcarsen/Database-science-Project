#Script for question 5
#Imports
import csv
from ProjectCode.Visualization import Vis
from ProjectCode.Calculations import Calc
#Data file
file = 'question5.csv'
def run():
    #array of post processed data
    data = []
    #post process the data
    with open(file, 'rb') as Data:
        read = csv.reader(Data)
        for i in Data:
            i = i.split()
            if len(i) == 4:
                for k in range(len(i)):
                    temp = str(i[k])
                    temp =  temp.replace("b", "")
                    temp = temp.replace("\'", "")
                    i[k] = temp
                data.append(i)
    #Used to keep track of what series we are looking for the episode ratings corresponding to the series
    seriesIndex = data[0][3]
    #Will hold the series rating of each series
    seriesRating = []
    #Will hold the average episode rating in each series
    avgEpisodeRating = []
    #Current series rating
    seriesRate = 0
    #Used to average the episode ratings
    count = 0
    #Sum of the episode ratings
    epiRating = 0
    #Parse through the data calculating average episode rating for each series
    for episode in data:
        if seriesIndex == episode[3]:
            epiRating += float(episode[0])
            seriesRate = float(episode[1])
            count += 1
        else:
            avgEpisodeRating.append(epiRating / count)
            seriesRating.append(seriesRate)
            count = 1
            epiRating = float(episode[1])
            seriesIndex = episode[3]
    print(seriesRating)
    print(avgEpisodeRating)
    #Calcualtes the correlation coeffecients for avg episode rating and series rating
    c1 = Calc(avgEpisodeRating, seriesRating)
    c1.correlation()
    #Plots the avg episode rating and series rating
    v1 = Vis(avgEpisodeRating, seriesRating, 'Average Episode Rating', 'Series Rating', 'Episode Ratings in a TV Series Vs TV Series Rating')
    v1.plot()
