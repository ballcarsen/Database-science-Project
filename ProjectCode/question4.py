#Script for question 4
#Imports
import csv
from ProjectCode import Visualization
from ProjectCode import Calculations
#Data file
file = "question4.csv"
def run():
    #data Array
    data = []
    #post process query
    with open(file, 'rb') as Data:
        read = csv.reader(Data)
        for i in Data:
            i = i.split()
            if len(i) == 6:
                for k in range(len(i)):
                    temp = str(i[k])
                    temp =  temp.replace("b", "")
                    temp = temp.replace("\'", "")
                    i[k] = temp
                data.append(i)
    #average facebok likes of the crew and revnue/budget ratio for each produciton
    avgLikes = []
    rev_budg = []
    #Parse through data to calculate the average and rev/budg
    for i in data:
        like1 = float(i[0])
        like2 = float(i[1])
        like3 = float(i[2])
        rev = i[4]
        budg = float(i[5]) / 1000000
        #removes outliers
        if (like1 + like2 + like3) / float(3) < 5000 and float(rev)/ float(budg) < 15:
            avgLikes.append((like1 + like2 + like3) / float(3))
            rev_budg.append(float(rev)/ float(budg))

    #Plots crew facebook likes vs revenue/budget ratio
    v1 = Visualization.Vis(avgLikes, rev_budg, 'Crew Popularity' , 'Revenue to Budget Ratio = Payout', 'Crew Popularity v.s. Payout')
    v1.plot()
    #Calcualates correlation coefficient of the facebook likes and rev/budg
    c1 = Calculations.Calc(avgLikes, rev_budg)
    c1.correlation()