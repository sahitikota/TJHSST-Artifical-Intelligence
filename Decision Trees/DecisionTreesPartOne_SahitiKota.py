# Sahiti Kota
# 04/19/2022
from math import log2
import sys

categories = []
data = []

fileName = sys.argv[1]

with open(fileName) as f:
    lineList = [line.lower().strip().split(",") for line in f]
    for lineNum in range(0, len(lineList)):
        categories = lineList[0]
        if lineNum > 0:
            row = {}
            for i in range(0, len(categories)):
                row[categories[i]] = lineList[lineNum][i]
            data.append(row)

def calculateEntropy(data, categories):
    finalOutcomes = {}
    finalOutcomeCategory = categories[-1]
    for row in data:
        if row[finalOutcomeCategory] not in finalOutcomes:
            finalOutcomes[row[finalOutcomeCategory]] = 1
        else:
            finalOutcomes[row[finalOutcomeCategory]] += 1
    entropy = 0
    for outcome in finalOutcomes:
        entropy += (finalOutcomes[outcome]/len(data)) * log2((finalOutcomes[outcome]/len(data)))
    return entropy * -1

def calculateInformationGain(feature, data):
    possibleValues = {}
    for row in data:
        if row[feature] in possibleValues:
            possibleValues[row[feature]].append(row)
        else:
            possibleValues[row[feature]] = [row]
    entropy = 0
    for value in possibleValues:
        entropy += (len(possibleValues[value])/len(data)) * calculateEntropy(possibleValues[value], categories)
    informationGain = calculateEntropy(data, categories) - entropy
    return informationGain

def generateTree(tree, data, categories):
    bestFeature = ''
    highestInfoGain = 0
    temp = categories[:len(categories) - 1]
    for feature in temp:
        infoGain = calculateInformationGain(feature, data)
        if infoGain > highestInfoGain:
            highestInfoGain = infoGain
            bestFeature = feature
    tree[bestFeature] = {}
    possibleValues = {}
    for row in data:
        if row[bestFeature] in possibleValues:
            possibleValues[row[bestFeature]].append(row)
        else:
            possibleValues[row[bestFeature]] = [row]
    for value in possibleValues:
        tree[bestFeature][value] = {}
        if calculateEntropy(possibleValues[value], categories) != 0:
            generateTree(tree[bestFeature][value], possibleValues[value], categories)   
        else:
            tree[bestFeature][value] = possibleValues[value][0][categories[len(categories) - 1]]     
    return tree

tree = {}
tree = generateTree(tree, data, categories)

f = open("treeout.txt", "w")
f.close()
f = open("treeout.txt", "r+")

def printTree(tree, data, categories, indent):
    for key, value in tree.items():
        f.write("   " * indent + "* " + str(key) + "?")
        if type(value) != dict:
            f.write(" -> " + str(value + "\n"))
        else:
            f.write("\n")
            printTree(value, data, categories, indent + 1)
    
printTree(tree, data, categories, 0)
f.close()
    

