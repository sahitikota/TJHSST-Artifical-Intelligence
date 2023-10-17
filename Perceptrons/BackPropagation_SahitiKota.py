# Sahiti Kota
# 05/27/2022
import sys
import math
import numpy as np
    
def step(num):
    if num > 0:
        return 1
    return 0
    
def sigmoid(num):
    value = (1/ (1 + math.e**(-num)))
    return value

def perceptron(A, w, b, x):
    for i in range(len(w)):
        b += (w[i] * x[i])
    return A(b)

def pNet(A, x, wList, bList):
    newA = np.vectorize(A)
    for layer in range(1, len(wList)):
        output = newA(x @ wList[layer] + bList[layer])
        x = output
    return output

def checkCircleAccuracy(point):
    if (point[0][0] ** 2 + point[0][1] ** 2) ** 0.5 < 1:
        return 1
    return 0

if sys.argv[1] == "S":
    numEpochs = 7500
    trainingSet = [(np.array([[0, 0]]), np.array([[0, 0]])), (np.array([[0, 1]]), np.array([[0, 1]])), (np.array([[1, 0]]), np.array([[0, 1]])), (np.array([[1, 1]]), np.array([[1, 0]]))]
    weightList = [None, 2 * np.random.rand(2, 2) - 1, 2 * np.random.rand(2, 2) - 1]
    biasList = [None, 2 * np.random.rand(1, 2) - 1, 2 * np.random.rand(1, 2) - 1]
    def train(wList, bList):
        newSigmoid = np.vectorize(sigmoid)
        for i in range(numEpochs):
            for data in trainingSet:
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
                print("Epoch", i, ":", a[len(a) - 1])
            print()
        return (wList, bList)
    weightList, biasList = train(weightList, biasList)    

elif sys.argv[1] == "C": 
    numEpochs = 1000
    trainingSet = []
    with open("10000_pairs.txt") as f:
        for line in f:
            x, y = line.split()
            point = np.array([[float(x), float(y)]])
            inOrOut = checkCircleAccuracy(point)
            trainingSet.append((point, np.array([[inOrOut]])))     
    weightList = [None, np.random.rand(2, 4), np.random.rand(4, 1)]
    biasList = [None, np.random.rand(1, 4), np.random.rand(1, 1), np.random.rand(1, 1)]
    def train(wList, bList):
        newSigmoid = np.vectorize(sigmoid)
        for i in range(numEpochs):
            for data in trainingSet:
                x, y = data
                a, dot, delta = [x], [None], [None] * len(wList)
                learningRate = 0.1
                N = len(wList) - 1
                for L in range(1, len(wList)):
                    dot.append((a[L - 1] @ wList[L]) + bList[L])
                    a.append(newSigmoid(dot[L]))
                delta[N] = (newSigmoid(dot[N]) * (1 - newSigmoid(dot[N]))) * (y - a[N])
                for L in range(N - 1, 0, -1):
                    delta[L] = (newSigmoid(dot[L]) * (1 - newSigmoid(dot[L]))) * (delta[L + 1] @ (wList[L + 1]).transpose())
                for L in range(1, len(wList)):
                    bList[L] = bList[L] + learningRate * delta[L]
                    wList[L] = wList[L] + learningRate * ((a[L-1]).T @ delta[L])
            numMisclassified = 0
            for point in trainingSet:
                if round(pNet(sigmoid, point[0][0], wList, bList)[0][0]) != point[1][0][0]:
                    numMisclassified += 1
            print("Epoch",i,":", numMisclassified)
            print(wList, bList)
        return (wList, bList)
    weightList, biasList = train(weightList, biasList)
