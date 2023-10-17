# Sahiti Kota
# 09/7/2021

import math
from math import factorial
from itertools import permutations

# Problem 12
def findFactors(num):
    factorsCount = 0
    for i in range(1, int((math.sqrt(num)) + 1)):
        if num % i == 0:
            factorsCount += 2
        if i ** 2 == num:
            factorsCount -= 1
    return factorsCount

def reachedNumFactors(num):
    triangle = 0
    for i in range(1, 10000000):
        triangle += i
        if findFactors(triangle) >= num:
            return triangle

print("12:", reachedNumFactors(500))

# Problem 14
def collatz(x):
    length = 0
    while x > 1:
        if x % 2 == 0:
            length += 1
            x = x/ 2
        elif x % 2 == 1:
            length += 1
            x = 3 * x + 1
    if x == 1:
        return length
maxLength = 0
maxLengthNum = 0
for i in range (999999, 2, -1):
    currentLength = collatz(i)
    if (currentLength > maxLength):
        maxLength = currentLength
        maxLengthNum = i
print("14:", maxLengthNum)

# Problem 16
'''sum = 0
numString = str(2 ** 1000)
numsList = [int(x) for x in numString[::1]]
for n in numsList:
    sum += n
print(sum)'''

# Problem 21
amicableNumbersSet= set()
def findFactorsSum(num):
    factorsTotal = 1
    for i in range(2, int((math.sqrt(num)) + 1)):
        if num % i == 0:
            factorsTotal += i
            if (num// i) > i:
                factorsTotal += (num// i)
    return factorsTotal

for i in range(1, 10000):
    iSum = findFactorsSum(i)
    for j in range(i + 1, 10000):
        if i != j and iSum == j and findFactorsSum(j) == i:
            amicableNumbersSet.add(i)
            amicableNumbersSet.add(j)

amicableNumbersSum = 0
for num in amicableNumbersSet:
    amicableNumbersSum += num

print("21:", amicableNumbersSum)

# Problem 24
permutationsList = list(permutations("0123456789"))
millionthPerm = "".join(permutationsList[999999])
print("24:" + millionthPerm)

# Problem 28
lastNum = 1001 * 1001
oddNumList =[]
numsUsedList =[]
for i in range (1, lastNum + 1, 2):
    oddNumList.append(i)
sum = 0
k = 0
gap = 1
while k <= len(oddNumList) - 1:
    if oddNumList[k] == lastNum:
        sum += int(oddNumList[k])
        print ("28:", sum)
    else:
        if (len(numsUsedList) == 4):
            gap += 1
            numsUsedList.clear()
        sum += int(oddNumList[k])
        numsUsedList.append(oddNumList[k])
    k += gap

# Problem 30
numList = []
finalSum = 0
largest = 5 * 9 ** 5 + 1
for hundredThousandth in range(0, 10):
    for tenThousand in range(0, 10):
        for thousand in range(0, 10):
            for hundred in range(0, 10):
                for ten in range(0, 10):
                    for one in range(0, 10):
                        value = one * 1 + ten * 10 + hundred * 100 + thousand * 1000 + tenThousand * 10000 + hundredThousandth * 100000
                        #print(value)
                        if (one ** 5 + ten ** 5 + hundred ** 5 + thousand ** 5 + tenThousand ** 5 + hundredThousandth  ** 5 == value):
                            numList.append(value)
                        elif value == largest:
                            for num in numList:
                                finalSum += int(num)
print("30:", finalSum - 1)


