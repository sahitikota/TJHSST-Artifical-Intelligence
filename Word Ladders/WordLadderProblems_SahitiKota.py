# Sahiti Kota
# 09/28/2021

from collections import deque

def getChildren(parentWord):
    childrenList = []
    for newWord in wordsList:
        difference = 0
        if len(newWord) == len(parentWord):
            for i in range(len(newWord)):
                if newWord[i] != parentWord[i]:
                    difference += 1
                if difference > 1:
                    continue
        if difference == 1:
            childrenList.append(newWord)
    return childrenList
def goalTest(originalWord, wordString):
    #value = [i for i, tuple in enumerate(startEndList) if tuple[0] == wordString]
    for tuple in startEndList:
        if tuple[0] == originalWord:
            if wordString == tuple[1]:
                return True

startEndList =[]
with open("puzzles_normal.txt") as f:
    lineList = [line.strip().split() for line in f]
    for lineNum in range(0, len(lineList)):
        startEndList.append(("".join(lineList[lineNum][0]), "".join(lineList[lineNum][1])))
overallList = []
def BFS(startBoard):
    ogParent = startBoard 
    visited = set()
    fringe = deque()
    fringe.append((startBoard, 0, [startBoard]))
    visited.add(startBoard)
    while fringe:
        parent, parentSteps, parentPath = fringe.popleft()
        '''if goalTest(ogParent, parent) == True:
            return parentSteps'''
        for child in getChildren(parent):
            if child not in visited:
                childPath = parentPath.copy()
                childPath.append(child)
                childSteps = parentSteps + 1
                fringe.append((child, childSteps, childPath))
                visited.add(child)
    overallList.append(visited)
    return None
print("done")

def maxLength(startBoard):
    maxSteps = -1
    ogParent = startBoard 
    visited = set()
    fringe = deque()
    visitedWithSteps = deque()
    fringe.append((startBoard, 1, [startBoard]))
    visited.add(startBoard)
    visitedWithSteps.append((startBoard, 0, [startBoard]))
    while fringe:
        parent, parentSteps, parentPath = fringe.popleft()
        for child in getChildren(parent):
            if child not in visited:
                childPath = parentPath.copy()
                childPath.append(child)
                childSteps = parentSteps + 1
                if childSteps > maxSteps:
                    maxSteps = childSteps
                fringe.append((child, childSteps, childPath))
                visited.add(child)
                visitedWithSteps.append((child, childSteps, childPath))
    overallList.append(visited)
    while visitedWithSteps:
        node, nodeSteps, nodePath = visitedWithSteps.popleft()
        if nodeSteps == maxSteps:
            return node, nodeSteps, nodePath
    return None

wordsList = []
with open("words_06_letters.txt") as f:
    lineList = [line.strip().split() for line in f]
    for lineNum in range(0, len(lineList)):
        wordsList.append("".join(lineList[lineNum]))
    for lineNum in range(0, len(lineList)):
        currentWord = "".join(lineList[lineNum])
        isIn = any(currentWord in sublist for sublist in overallList)
        if isIn == False:
            BFS("".join(lineList[lineNum]))

maximum = max([len(i) for i in overallList])
#print("max:", maximum)
#print("number:", len(overallList) - 1568)
for i in overallList:
    if len(i) == maximum:
        maxCluster = i

longestLength = 0
item = maxCluster.pop()
longestLength = (maxLength(item)[1])
item = (maxLength(item)[0])
print(longestLength)
print(maxLength(item)[1])
while longestLength != (maxLength(item)[1]):
        item = (maxLength(item)[0])
        longestLength = (maxLength(item)[1])
if longestLength == (maxLength(item)[1]):
    print((maxLength(item)[2]), longestLength)

#problem #4, find longest path of a random one from set. 
#afterwards cehck he longest path from thatg on e and thne longets frlom 
# that and on and oln,an d you'lll know ikt is the longest path 
# when thne node reached's longest apth is the path taken to reach it