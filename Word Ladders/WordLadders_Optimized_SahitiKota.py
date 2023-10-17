# Sahiti Kota
# 12/20/2021

from collections import deque
import sys
import time
from collections import defaultdict

sixLettersFileName = sys.argv[1]
puzzlesFileName = sys.argv[2]

def goalTest(originalWord, wordString):
    for start, end in startEndDict.items():
        if start == originalWord:
            if wordString == end:
                return True

def BFS(startBoard):
    ogParent = startBoard 
    visited = set()
    fringe = deque()
    fringe.append((startBoard, 1, [startBoard]))
    visited.add(startBoard)
    while fringe:
        parent, parentSteps, parentPath = fringe.popleft()
        if goalTest(ogParent, parent) == True:
            return parentPath
        for child in getChildren(parent):
            if child not in visited:
                childPath = parentPath.copy()
                childPath.append(child)
                childSteps = parentSteps + 1
                fringe.append((child, childSteps, childPath))
                visited.add(child)
    return ["No Solution!"]

def findGoal(originalWord):
    return startEndDict[originalWord]

def BiBFS(startBoard):
    visitedStart = set()
    fringeStart = deque()
    visitedTarget = set()
    visitedStartSteps = {}
    visitedTargetSteps = {}
    fringeTarget = deque()
    targetBoard = findGoal(startBoard)
    visitedStart.add(startBoard)
    fringeStart.append((startBoard, 1, [startBoard]))
    visitedTarget.add(targetBoard)
    fringeTarget.append((targetBoard, 1, [targetBoard]))
    while fringeStart and fringeTarget:
        if fringeStart:
            parent, parentSteps, parentPath = fringeStart.popleft()
            for child in getChildren(parent):
                if child in visitedTarget:
                    childPath = parentPath.copy()
                    childPath.append(child)
                    childSteps = parentSteps + 1
                    if len(visitedTargetSteps) > 0:
                        (visitedTargetSteps[child][1]).reverse()
                        (visitedTargetSteps[child][1]).pop(0)
                        return childPath + (visitedTargetSteps[child][1])
                    else:
                        return childPath
                elif child not in visitedStart:
                    childPath = parentPath.copy()
                    childPath.append(child)
                    childSteps = parentSteps + 1
                    fringeStart.append((child, childSteps, childPath))
                    visitedStart.add(child)
                    visitedStartSteps[child] = (childSteps, childPath)
        if fringeTarget:
            parent, parentSteps, parentPath = fringeTarget.popleft()
            for child in getChildren(parent):
                if child in visitedStart:
                    childPath = parentPath.copy()
                    childPath.append(child)
                    childSteps = parentSteps + 1
                    (childPath).reverse()
                    (childPath).pop(0)
                    return (visitedStartSteps[child][1]) + childPath
                elif child not in visitedTarget:
                    childPath = parentPath.copy()
                    childPath.append(child)
                    childSteps = parentSteps + 1
                    fringeTarget.append((child, childSteps, childPath))
                    visitedTarget.add(child)
                    visitedTargetSteps[child] = (childSteps, childPath)
    return ['No Solution!']

'''wordsSet = set()
wordsListLength = 0
with open(sixLettersFileName) as f:
    lineList = [line.strip() for line in f]
    start = time.perf_counter()
    for lineNum in range(0, len(lineList)):
        wordsSet.add("".join(lineList[lineNum]))
        wordsListLength += 1
    end = time.perf_counter()
    print("Time to create this data structure was:", (end - start), "seconds")
    print("There are", wordsListLength, "words in this dict.", "\n")'''

buckets = defaultdict(set)
wordsGraph = defaultdict(set)
wordsListLength = 0
with open(sixLettersFileName) as f:
    lineList = [line.strip() for line in f]
    start = time.perf_counter()
    for lineNum in range(0, len(lineList)):
        word = "".join(lineList[lineNum])
        wordsListLength += 1
        for index in range(len(word)):
            key = word[:index] + '_' + word[index + 1:]
            buckets[key].add(word)
    end = time.perf_counter()
    print("Time to create this data structure was:", (end - start), "seconds")
    print("There are", wordsListLength, "words in this dict.", "\n")

def getChildren(parentWord):
    ''''childrenSet = set()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for index in range(6):
        for letter in alphabet:
            word = parentWord[:index] + letter + parentWord[index + 1:] 
            if word in wordsSet and word != parentWord:
                childrenSet.add(word)
    return childrenSet'''
    cSet = []
    childrenSet = []
    for index in range(len(parentWord)):
        key = parentWord[:index] + '_' + parentWord[index + 1:]
        cSet.append(buckets[key])
    for s in cSet:
        for item in s:
            if item != parentWord:
                childrenSet.append(item)
    return childrenSet
    
startEndDict = {}
with open(puzzlesFileName) as f:
    lineList = [line.strip().split() for line in f]
    lineListLength = len(lineList)
    for lineNum in range(0, lineListLength):
        startEndDict["".join(lineList[lineNum][0])] = "".join(lineList[lineNum][1])

with open(puzzlesFileName) as f:
    lineList = [line.strip().split() for line in f]
    lineListLength = len(lineList) 
    start = time.perf_counter()  
    for lineNum in range(0, lineListLength):
        print("Line:", lineNum)
        path = BiBFS("".join(lineList[lineNum][0]))
        if len(path) > 1:
            print("Length is:", len(path))
        for word in path:
            print(word)
        print("\n")
    end = time.perf_counter()
    print("Time to solve all of these puzzles was", (end - start), "seconds")

