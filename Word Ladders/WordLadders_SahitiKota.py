# Sahiti Kota
# 09/28/2021

from collections import deque
import sys
import time

sixLettersFileName = sys.argv[1]
puzzlesFileName = sys.argv[2]

def getChildren(parentWord):
    childrenList = []
    for newWord in wordsList:
        difference = 0
        for i in range(len(newWord)):
            if newWord[i] != parentWord[i]:
                difference += 1
            if difference > 1:
                continue
        if difference == 1:
            childrenList.append(newWord)
    return childrenList

def goalTest(originalWord, wordString):
    # value = [i for i, tuple in enumerate(startEndList) if tuple[0] == originalWord]
    for tuple in startEndList:
        if tuple[0] == originalWord:
            if wordString == tuple[1]:
                return True

def BFS(startBoard):
    ogParent = startBoard 
    visited = set()
    fringe = deque()
    extra = deque()
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

wordsList = []
wordsListLength = 0
with open(sixLettersFileName) as f:
    lineList = [line.strip().split() for line in f]
    start = time.perf_counter()
    for lineNum in range(0, len(lineList)):
        wordsList.append("".join(lineList[lineNum]))
        wordsListLength += 1
    end = time.perf_counter()
    print("Time to create this data structure was:", (end - start), "seconds")
    print("There are", wordsListLength, "words in this dict.", "\n")

startEndList = []
with open(puzzlesFileName) as f:
    lineList = [line.strip().split() for line in f]
    lineListLength = len(lineList)
    for lineNum in range(0, lineListLength):
        startEndList.append(("".join(lineList[lineNum][0]), "".join(lineList[lineNum][1])))
    start = time.perf_counter()
    for lineNum in range(0, lineListLength):
        print("Line:", lineNum)
        path = BFS("".join(lineList[lineNum][0]))
        if len(path) > 1:
            print("Length is:", len(path))
        for word in path:
            print(word)
        print("\n")
    end = time.perf_counter()
    print("Time to solve all of these puzzles was", (end - start), "seconds")