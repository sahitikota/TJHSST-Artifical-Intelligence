# Sahiti Kota
# 10/12/2021

import sys
import heapq
import time
from math import pi, acos, sin, cos

def calcd(node1, node2):
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees
   y1, x1 = node1
   y2, x2 = node2

   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

nodeDictionary = dict()
with open('rrNodes.txt') as f:
    lineList = [line.strip().split() for line in f]
    for lineNum in range(0, len(lineList)):
        currentJunction = "".join(lineList[lineNum][0])
        nodeDictionary[currentJunction] = (float(lineList[lineNum][1]), float(lineList[lineNum][2]))

junctionDictionary = dict()
junctionDictionary.setdefault(list)
start = time.perf_counter()
with open('rrEdges.txt') as f:
    lineList = [line.strip().split() for line in f]
    for lineNum in range(0, len(lineList)):
        startJunction = "".join(lineList[lineNum][0])
        endJunction = "".join(lineList[lineNum][1])
        if startJunction in junctionDictionary:
            junctionDictionary[startJunction].append((endJunction, calcd(nodeDictionary[endJunction], nodeDictionary[startJunction])))
        else:
            junctionDictionary[startJunction] = [(endJunction, calcd(nodeDictionary[endJunction], nodeDictionary[startJunction]))]
        if endJunction in junctionDictionary:
            junctionDictionary[endJunction].append((startJunction, calcd(nodeDictionary[endJunction], nodeDictionary[startJunction])))
        else:
            junctionDictionary[endJunction] = [(startJunction, calcd(nodeDictionary[endJunction], nodeDictionary[startJunction]))]
end = time.perf_counter()

print("Time to create data structure: " + str(end - start))

junctionCityDictionary = dict()
with open('rrNodeCity.txt') as f:
    lineList = [line.strip().split() for line in f]
    for lineNum in range(0, len(lineList)):
        junction = "".join(lineList[lineNum][0])
        junctionCity = " ".join(lineList[lineNum][1:])
        junctionCityDictionary[junction] = junctionCity

flippedJunctionCityDictionary = dict()
with open('rrNodeCity.txt') as f:
    lineList = [line.strip().split() for line in f]
    for lineNum in range(0, len(lineList)):
        junction = "".join(lineList[lineNum][0])
        junctionCity = " ".join(lineList[lineNum][1:])
        flippedJunctionCityDictionary[junctionCity] = junction

def goalTest(currentJunction, endJunction):
    if currentJunction == endJunction:
        return True

def getChildren(currentJunction):
    endNamesList = []
    endJunctionsList = junctionDictionary[currentJunction]
    for junction in endJunctionsList:
        name, distance = junction
        endNamesList += [name]
    return endNamesList

def djikstra(startJunction, endJunction):
    start = time.perf_counter()
    closed = set()
    fringe = []
    heapq.heapify(fringe)
    heapq.heappush(fringe, (0, startJunction))
    while fringe:
        parentDepth, parent = heapq.heappop(fringe)
        if goalTest(parent, endJunction) == True:
            end = time.perf_counter()
            return junctionCityDictionary[startJunction] + " to " + junctionCityDictionary[endJunction] + " with Djikstra: " + str(parentDepth) + " in " + str(end - start) + " seconds"
        if parent not in closed:
            closed.add(parent)
            for child in getChildren(parent):
                if child not in closed:
                    parentJunctionDict = junctionDictionary[parent]
                    for item in parentJunctionDict:
                        if item[0] == child:
                            childDepth = parentDepth + item[1]
                    heapq.heappush(fringe, (childDepth, child))
    return None

def aStar(startJunction, endJunction):
    start = time.perf_counter()
    closed = set()
    fringe = []
    heapq.heapify(fringe)
    heapq.heappush(fringe, (calcd(nodeDictionary[endJunction], nodeDictionary[startJunction]), 0, startJunction))
    while fringe:
        parentEstimateGreatCircle, parentDepth, parent = heapq.heappop(fringe)
        if goalTest(parent, endJunction) == True:
            end = time.perf_counter()
            return junctionCityDictionary[startJunction] + " to " + junctionCityDictionary[endJunction] + " with A*: " + str(parentDepth) + " in " + str(end - start) + " seconds"
        if parent not in closed:
            closed.add(parent)
            for child in getChildren(parent):
                if child not in closed:
                    parentJunctionDict = junctionDictionary[parent]
                    for item in parentJunctionDict:
                        if item[0] == child:
                            childDepth = parentDepth + item[1]
                    childEstimateGreatCircle = childDepth + calcd(nodeDictionary[endJunction], nodeDictionary[child])
                    heapq.heappush(fringe, (childEstimateGreatCircle, childDepth, child))
    return None

startCityName = sys.argv[1]
endCityName = sys.argv[2]

startJunction = flippedJunctionCityDictionary[startCityName]
endJunction = flippedJunctionCityDictionary[endCityName]
print(djikstra(startJunction, endJunction))
print(aStar(startJunction, endJunction))