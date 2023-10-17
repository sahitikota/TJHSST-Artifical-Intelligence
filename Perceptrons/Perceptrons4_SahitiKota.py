# Sahiti Kota
# 05/19/2022

import numpy as np
import sys
import ast
import math
import random

def step(num):
    if num > 0:
        return 1
    return 0

XORweightLayerOne = np.array([[1, -1], [1, -2]])
XORweightLayerTwo = np.array([[1], [2]])
XORweightMatrices = [None, XORweightLayerOne, XORweightLayerTwo]
XORbiasLayerOne = np.array([[0, 3]])
XORbiasLayerTwo = np.array([[-2]])
XORbiases = [None, XORbiasLayerOne, XORbiasLayerTwo]

def pNet(A, x, wList, bList):
    newA = np.vectorize(A)
    for layer in range(1, len(wList)):
        output = newA(x @ wList[layer] + bList[layer])
        x = output
    return output

diamondWeightLayerOne = np.array([[1, -1, 1, -1], [1, 1, -1, -1]])
diamondWeightLayerTwo = np.array([[1], [1], [1], [1]])
diamondWeightMatrices = [None, diamondWeightLayerOne, diamondWeightLayerTwo]
diamondBiasLayerOne = np.array([[1, 1, 1, 1]])
diamondBiasLayerTwo = np.array([[-3]])
diamondBiases = [None, diamondBiasLayerOne, diamondBiasLayerTwo]

def sigmoid(num):
    value = (1/ (1 + math.e**(-num)))
    return value

def checkCircleAccuracy(point):
    if (point[0][0] ** 2 + point[0][1] ** 2) ** 0.5 < 1:
        return 1
    return 0

biasOne = 1.378
biasTwo = -3.2

circleWeightLayerOne = np.array([[1, -1, 1, -1], [1, 1, -1, -1]])
circleWeightLayerTwo = np.array([[1], [1], [1], [1]])
circleWeightMatrices = [None, circleWeightLayerOne, circleWeightLayerTwo]
circleBiasLayerOne = np.array([[biasOne, biasOne, biasOne, biasOne]])
circleBiasLayerTwo = np.array([[biasTwo]])
circleBiases = [None, circleBiasLayerOne, circleBiasLayerTwo]

if len(sys.argv) == 2:
    input = sys.argv[1]
    x, y = ast.literal_eval(input)
    # XOR happens here
    print(pNet(step, np.array([x, y]), XORweightMatrices, XORbiases))
elif len(sys.argv) == 3:
    inOrOut = pNet(step, np.array([float(sys.argv[1]), float(sys.argv[2])]), diamondWeightMatrices, diamondBiases)
    if inOrOut == [[0]]:
        print("outside")
    else:
        print("inside")
elif len(sys.argv) == 1:
    points = []
    for point in range(500):
        points.append([[np.random.uniform(-1, 1), np.random.uniform(-1, 1)]])
    accuracies = 0
    for point in points:
        value = pNet(step, point, circleWeightMatrices, circleBiases)
        if value[0][0] >= 0.5:
            pValue = 1
        else:
            pValue = 0
        if checkCircleAccuracy(point) == pValue:
            accuracies += 1
    print(accuracies/500 * 100, "%")