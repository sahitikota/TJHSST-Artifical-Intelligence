# Sahiti Kota
# 04/26/2022
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

def addVectors(w, x):
    newVect = []
    for i in range(len(w)):
        newVect.append((w[i] + x[i])) 
    # print(newVect)
    return tuple(newVect)
    
# 2 bit, 6 and 9 are functions that don't work
def determineNumFuncs(bits):
    accurate = 0
    delta = 1
    for n in range(2**(2**bits)):
        truthT = truthTable(bits, n)
        # printTruthTable(truthT)
        if bits == 2:
            weight = (0, 0)
            lastWeight = (0, 0)
        elif bits == 3:
            weight = (0, 0, 0)
            lastWeight = (0, 0, 0)
        elif bits == 4:
            weight = (0, 0, 0, 0)
            lastWeight = (0, 0, 0, 0)
        bias = 0
        lastBias = 0
        epochs = 0
        while epochs < 100:
            for x in truthT.keys():
                f = perceptron(step, weight, bias, x)
                newWeight = []
                for value in x:
                    newWeight.append((value * (truthT[x] - f) * delta))
                weight = addVectors(tuple(newWeight), weight)
                bias = bias + ((truthT[x] - f) * delta)
                # print(x, weight, bias)
            if epochs > 0 and weight == lastWeight and bias == lastBias:
                numCorrect = 0
                for x in truthT.keys():
                    f = perceptron(step, weight, bias, x)
                    if truthT[x] == f:
                        numCorrect += 1
                if numCorrect == 2**bits:
                    accurate += 1
                    break
            lastWeight = weight
            lastBias = bias
            epochs += 1
    print((2**(2** bits)), "possible functions;", accurate, "can be correctly modeled.")

def trainPerceptron(bits, n):
    complete = False
    accurate = 0
    delta = 1
    truthT = truthTable(bits, n)
    # printTruthTable(truthT)
    if bits == 2:
        weight = (0, 0)
        lastWeight = (0, 0)
    elif bits == 3:
        weight = (0, 0, 0)
        lastWeight = (0, 0, 0)
    elif bits == 4:
        weight = (0, 0, 0, 0)
        lastWeight = (0, 0, 0, 0)
    bias = 0
    lastBias = 0
    epochs = 0
    while epochs < 100:
        for x in truthT.keys():
            f = perceptron(step, weight, bias, x)
            newWeight = []
            for value in x:
                newWeight.append((value * (truthT[x] - f) * delta))
            weight = addVectors(tuple(newWeight), weight)
            bias = bias + ((truthT[x] - f) * delta)
            # print(x, weight, bias)
        if epochs > 0 and weight == lastWeight and bias == lastBias:
            numCorrect = 0
            for x in truthT.keys():
                f = perceptron(step, weight, bias, x)
                if truthT[x] == f:
                    numCorrect += 1
            if numCorrect == 2**bits:
                accurate += 1
                print("Final Weight Vector:", weight)
                print("Final Bias Value:", bias)
                print("Accuracy:", 1)
                complete = True
                break
        lastWeight = weight
        lastBias = bias
        epochs += 1
    if complete == False:
        print("Final Weight Vector:", weight)
        print("Final Bias Value:", bias)
        numCorrect = 0
        for x in truthT.keys():
            f = perceptron(step, weight, bias, x)
            if truthT[x] == f:
                numCorrect += 1
        print("Accuracy:", float(numCorrect/ 2**bits))

# bits = int(sys.argv[1])
# n = int(sys.argv[2])

print(trainPerceptron(2, 15))
printTruthTable(truthTable(2, 15))

    
