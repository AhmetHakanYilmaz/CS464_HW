import csv
from math import log
import math

trainData = list(csv.reader(open('bbcsports_train.csv')))
valData = list(csv.reader(open('bbcsports_val.csv')))

lengthsOfClasses = [0, 0, 0, 0, 0] # lengths of classes for training
lengthsOfClassesForVal = [0, 0, 0, 0, 0]  # lengths of classes for validation
totalLength = 0  # total length of training set
totalLengthForVal = 0 # total lengths of training set

#calculation for lengths of classes in training set
for i in range(1,len(trainData)):
    if int(trainData[i][4613]) == 0:
        lengthsOfClasses[0] = lengthsOfClasses[0]+1
    elif int(trainData[i][4613])== 1:
        lengthsOfClasses[1] = lengthsOfClasses[1]+1
    elif int(trainData[i][4613]) == 2:
        lengthsOfClasses[2] = lengthsOfClasses[2]+1
    elif int(trainData[i][4613]) == 3:
        lengthsOfClasses[3] = lengthsOfClasses[3]+1
    elif int(trainData[i][4613])== 4:
        lengthsOfClasses[4] = lengthsOfClasses[4]+1
    totalLength = totalLength+1
#print(lengthsOfClasses)
#print(totalLength)

#calculation for lengths of classes in validation set
for i in range(1,len(valData)):
    if int(valData[i][4613]) == 0:
        lengthsOfClassesForVal[0] = lengthsOfClassesForVal[0]+1
    elif int(valData[i][4613])== 1:
        lengthsOfClassesForVal[1] = lengthsOfClassesForVal[1]+1
    elif int(valData[i][4613]) == 2:
        lengthsOfClassesForVal[2] = lengthsOfClassesForVal[2]+1
    elif int(valData[i][4613]) == 3:
        lengthsOfClassesForVal[3] = lengthsOfClassesForVal[3]+1
    elif int(valData[i][4613])== 4:
        lengthsOfClassesForVal[4] = lengthsOfClassesForVal[4]+1
#print(lengthsOfClassesForVal)
#print(totalLengthForVal)


model = [[0 for x in range(4613)] for y in range(5)] #model for each class and word number of words from that class and that word
sumForClasses = [0,0,0,0,0] # sum of the words number in each class
matrix = [[0 for x in range(5)] for y in range(5)] #confusion matrix


for i in range(0,4613):
    for j in range(1,len(trainData)):
        if int(trainData[j][4613]) == 0:
            model[0][i] = model[0][i] + int(trainData[j][i])
            sumForClasses[0] = sumForClasses[0] +  int(trainData[j][i])
        elif int(trainData[j][4613]) == 1:
            model[1][i] = model[1][i] + int(trainData[j][i])
            sumForClasses[1] = sumForClasses[1] + int(trainData[j][i])
        elif int(trainData[j][4613]) == 2:
            model[2][i] = model[2][i] + int(trainData[j][i])
            sumForClasses[2] = sumForClasses[2] + int(trainData[j][i])
        elif int(trainData[j][4613]) == 3:
            model[3][i] = model[3][i] + int(trainData[j][i])
            sumForClasses[3] = sumForClasses[3] + int(trainData[j][i])
        elif int(trainData[j][4613]) == 4:
            model[4][i] = model[4][i] + int(trainData[j][i])
            sumForClasses[4] = sumForClasses[4] + int(trainData[j][i])

#print(sumForClasses)

predictionVal = [0] * len(valData) #prediction array for validation set      
count = 0 #correct predictions
totalCount = 0 #total predictions
for i in range(1,len(valData)):
    trueClass = -1
    for j in range(0,5):
        arg = log(lengthsOfClasses[j]/totalLength) 
        for k in range(0,4613):
            #For part 2.2 take the below if and else out of comment. For part 2.3 and smoothing take them in comment line 
            if model[j][k] != 0:
                arg =arg + int(valData[i][k]) * log ( (model[j][k]) / (sumForClasses[j]))
            else:
                arg = arg + int(valData[i][k]) * -math.inf

            #For part 2.3 and smoothing take the below line out of comment. For part 2.2 take it in comment line
            #arg =arg + int(valData[i][k]) * log ( (model[j][k]+1) / (sumForClasses[j] +4613)) 
        if j == 0:
            maxArg = arg
            trueClass = 0
        elif arg >= maxArg:
            maxArg = arg
            trueClass = j
    predictionVal[i] = trueClass
    totalCount= totalCount+1
    if predictionVal[i] == int(valData[i][4613]):
        count = count + 1
    matrix[predictionVal[i]][int(valData[i][4613])] = matrix[predictionVal[i]][int(valData[i][4613])] +1
    print("For the article", i,"predicted value is",predictionVal[i],"the correct value is",int(valData[i][4613]) )


#print("Predicted values",predictionVal)
print("Correct prediction rate", count, "/" ,totalCount)
print("Confusion matrix",matrix)
