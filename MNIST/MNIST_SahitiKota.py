# Sahiti Kota
# 06/02/2022

import random
import pickle
import numpy as np
import math

'''trainingSet = []
with open("mnist_train.csv.crdownload") as f:
    for line in f:
        line = line.strip().split(",")
        x = np.empty((1, 784))
        y = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        y[0,int(line[0])] = 1
        for i in range(1, len(line)):
            x[0, i-1] = int(line[i])/255 
        trainingSet.append((x, y))

file = open("trainingSet.pkl", 'wb')
pickle.dump(trainingSet, file)
file.close()'''

file = open("trainingSet.pkl", 'rb')
trainingSet = pickle.load(file)

weightList = [None, 2 * np.random.rand(784, 300) - 1, 2 * np.random.rand(300, 100) - 1, 2 * np.random.rand(100, 10) - 1]
biasList = [None, 2 * np.random.rand(1, 300) - 1, 2 * np.random.rand(1, 100) - 1, 2 * np.random.rand(1, 10) - 1]

def sigmoid(num):
    value = (1/ (1 + math.e**(-num)))
    return value

def pNet(A, x, wList, bList):
    newA = np.vectorize(A)
    for layer in range(1, len(wList)):
        output = newA(x @ wList[layer] + bList[layer])
        x = output
    return output

numEpochs = 100
def checkAccuracy(weightList, biasList, epoch, data):
    numMisclassified = 0
    for point in data:
        if np.argmax(pNet(sigmoid, point[0], weightList, biasList)) != np.where(point[1] == 1)[1][0]:
            numMisclassified += 1
    print("Epoch", epoch, ":", numMisclassified/len(data))
    
def train(wList, bList, dataSet):
    newSigmoid = np.vectorize(sigmoid)
    checkAccuracy(wList, bList, 0, dataSet)
    for i in range(numEpochs):
        for data in dataSet:
            x, y = data
            a, dot, delta = [x], [None], [None] * len(wList)
            learningRate = 0.1
            n = len(wList) - 1
            for layer in range(1, len(wList)):
                dot.append((a[layer - 1] @ wList[layer]) + bList[layer])
                a.append(newSigmoid(dot[layer]))
            delta[n] = (newSigmoid(dot[n]) * (1 - newSigmoid(dot[n]))) * (y - a[n])
            for layer in range(n - 1, 0, -1):
                delta[layer] = (newSigmoid(dot[layer]) * (1 - newSigmoid(dot[layer]))) * (delta[layer + 1] @ (wList[layer + 1]).T)
            for layer in range(1, len(wList)):
                bList[layer] = bList[layer] + learningRate * delta[layer]
                wList[layer] = wList[layer] + learningRate * ((a[layer-1]).transpose() @ delta[layer])
        file = open("MNISTNetwork.pkl", 'wb')
        pickle.dump((wList, bList), file)
        file.close()
        checkAccuracy(wList, bList, i + 1, dataSet)
    return (wList, bList)

weightList, biasList = train(weightList, biasList, trainingSet)