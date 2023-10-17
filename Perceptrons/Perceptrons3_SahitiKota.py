# Sahiti Kota
# 05/10/2022
import ast
import sys

def step(num):
    if num > 0:
        return 1
    return 0

def perceptron(A, w, b, x):
    for i in range(len(w)):
        b += (w[i] * x[i])
    return A(b)

# XOR HAPPENS HERE
def XOR(x):
    perceptron3 = perceptron(step, (1, 1), 0, x)
    perceptron4 = perceptron(step, (-1, -2), 3, x)
    perceptron5 = (perceptron3, perceptron4)
    return perceptron(step, (1, 2), -2, perceptron5)

input = sys.argv[1]
print(XOR(ast.literal_eval(input)))