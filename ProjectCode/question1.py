import csv
import pandas
import numpy as np
from ProjectCode import Visualization
from ProjectCode import Calculations


file = "question1.csv"
f = open(file)
f.readline()
#data = pandas.read_csv(file, sep = ",")
#print(data)
data = []
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

Budget = []
directorPopularity= []
compare = data[0][4]
budget = 0
rating = 0
count = 0
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

vis1 = Visualization.Vis(Budget, directorPopularity)
vis1.plot()
calc = Calculations.Calc(Budget, directorPopularity)
calc.spearmans()

