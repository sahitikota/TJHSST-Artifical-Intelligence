# Sahiti Kota
# 04/25/2022
import ast
import sys

def generateAllBinaryStrings(n, a, overallList):
    if n < 1:
        overallList.append(''.join(a))
    else:
        a[n-1] = '0'
        generateAllBinaryStrings(n - 1, a, overallList)
        a[n-1] = '1'
        generateAllBinaryStrings(n - 1, a, overallList)
    return(overallList)

def generateBinary(n):
    binary = str(bin(n).replace("0b", ""))
    return binary

def truthTable(bits, n):
    binary =  generateBinary(n)
    while len(binary) < 2 ** bits:
        binary = "0" + binary
    binaryList = generateAllBinaryStrings(bits, [None] * bits, [])
    binaryList.sort(reverse = True)
    pairs = {}
    for num in range(len(binaryList)):
        pairs[(tuple(map(int, binaryList[num])))] = int(binary[num])
    return pairs

def printTruthTable(pairs):
    for ins, out in pairs.items():
        string = ""
        for i in ins:
            string += str(i) + " "
        string += "| " + str(out)
        print(string)

def step(num):
    if num > 0:
        return 1
    return 0

def perceptron(A, w, b, x):
    for i in range(len(w)):
        b += (w[i] * x[i])
    return A(b)


def check(n, w, b):
    wT = ast.literal_eval(w)
    accuracyCount = 0
    truthT = truthTable(len(wT), n)
    for x in truthT.keys():
        percep = perceptron(step, wT, b, x)
        if percep == truthT[x]:
            accuracyCount += 1
    return float(accuracyCount)/2 ** len(wT)

n = int(sys.argv[1])
w = sys.argv[2]
b = float(sys.argv[3])
print(check(n, w, b))





    

