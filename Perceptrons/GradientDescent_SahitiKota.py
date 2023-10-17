# Sahiti Kota
# 05/26/2022
import sys
import numpy as np

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
count = 0
learningRate = 0.1
l = 9
yyv = "A"
if yyv == 'A':
    while l == 9:
        oldX = x
        oldY = y
        x = oldX - (learningRate * pDerivAX(oldX, oldY))
        y = oldY - (learningRate * pDerivAY(oldX, oldY))
        print("Location:", tuple([oldX, oldY]), "Gradient Vector:", tuple([-learningRate * pDerivAX(oldX, oldY), - learningRate * pDerivAY(oldX, oldY)]))
        if np.linalg.norm(np.array([-learningRate * pDerivAX(x, y), -learningRate * pDerivAY(x, y)])) < (10 ** (-8)):
            break
else:
    while l == 9:
        oldX = x
        oldY = y
        x = oldX - (learningRate * pDerivBX(oldX, oldY))
        y = oldY - (learningRate * pDerivBY(oldX, oldY))
        print("Location:", tuple([oldX, oldY]), "Gradient Vector:", tuple([-learningRate * pDerivBX(oldX, oldY), - learningRate * pDerivBY(oldX, oldY)]))
        if np.linalg.norm(np.array([-learningRate * pDerivBX(x, y), -learningRate * pDerivBY(x, y)])) < (10 ** (-8)):
            break