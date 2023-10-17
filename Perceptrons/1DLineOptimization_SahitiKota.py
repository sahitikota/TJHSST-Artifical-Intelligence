# Sahiti Kota
# 05/29/2022
import math
import sys
import numpy as np

def oneDMinimize(f, left, right, tolerance):
    if right - left < tolerance:
        return (right + left)/2
    else:
        third = (right - left)/3
        oneThird = left + third
        twoThird = left + (2 * third)
        leftVal = f(oneThird)
        rightVal =  f(twoThird)
        if leftVal > rightVal:
            return oneDMinimize(f, oneThird, right, (10 ** -8))
        else:
            return oneDMinimize(f, left, twoThird, (10 ** -8))

def funcA(x, y):
    return 4 * (x ** 2) - (3 * x * y) + 2 * (y ** 2) + (24 * x) - (20 * y)

def funcB(x, y):
    return ((1 - y) ** 2) + (x - (y ** 2)) ** 2

def pDerivAX(x, y):
    return (8 * x) - (3 * y) + 24

def pDerivAY(x, y):
    return (4 * y) - (3 * x) - 20

def pDerivBX(x, y):
    return (2 * (x - (y ** 2)))

def pDerivBY(x, y):
    return (-2 * (1- y)) - ((4 * y) * (x - (y ** 2)))

x = 0
y = 0

if sys.argv[1] ==  'A':
    while True:
        def changeLamb(learningRate):
            return funcA(x - learningRate * pDerivAX(x, y), y - learningRate * pDerivAY(x, y))
        learningRate = oneDMinimize(changeLamb, 0, 1, 10 ** -8)
        x = x - (learningRate * pDerivAX(x, y))
        y = y - (learningRate * pDerivAY(x, y))
        print("Location:", tuple([x, y]), "Gradient Vector:", tuple([pDerivAX(x, y), pDerivAY(x, y)]))
        if np.linalg.norm(np.array([pDerivAX(x, y), pDerivAY(x, y)])) <= (10 ** -8):
            break
elif sys.argv[1] == 'B':
    while True:
        def changeLamb(learningRate):
                return funcB(x - learningRate * pDerivBX(x, y), y - learningRate * pDerivBY(x, y))
        learningRate = oneDMinimize(changeLamb, 0, 1, 10 ** -8)
        x = x - (learningRate * pDerivBX(x, y))
        y = y - (learningRate * pDerivBY(x, y))
        print("Location:", tuple([x, y]), "Gradient Vector:", tuple([pDerivBX(x, y), pDerivBY(x, y)]))
        if np.linalg.norm(np.array([pDerivBX(x, y), pDerivBY(x, y)])) <= (10 ** -8):
            break
