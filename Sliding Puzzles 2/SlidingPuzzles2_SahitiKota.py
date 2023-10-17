# Sahiti Kota
# 10/04/2021

from collections import deque
import heapq
import sys
import time

fileName = sys.argv[1]

def parityCheck(stringRepresentation):
    boardSize = len(stringRepresentation) ** 0.5
    outOfOrderPairs = 0
    for i in range(len(stringRepresentation)):
        for j in range(i + 1, len(stringRepresentation)):
            if(stringRepresentation[i] != "." and stringRepresentation[j] != "."):
                if(stringRepresentation[i] > stringRepresentation[j]):
                    outOfOrderPairs += 1
    if boardSize % 2 == 1:
        if outOfOrderPairs % 2 == 0:
            return True
        else:
            return False
    elif boardSize % 2 == 0:
        if int(stringRepresentation.find(".") / boardSize) % 2 == 1:
            if outOfOrderPairs % 2 == 0:
                return True
            else:
                return False
        if int(stringRepresentation.find(".") / boardSize) % 2 == 0:
            if outOfOrderPairs % 2 == 1:
                return True
            else:
                return False

def getChildren(stringRepresentation):
    childrenList = []
    dotIndex = stringRepresentation.index(".")
    boardSize = len(stringRepresentation) ** 0.5
    boardList = list(stringRepresentation)
    # move left
    if(((dotIndex - 1) > -1) and ((dotIndex - 1) < len(boardList)) and ((dotIndex % boardSize) != 0)):
        boardList.insert(boardList.index(".") - 1, boardList.pop(boardList.index(".")))
        boardString = "".join(boardList)
        childrenList.append(boardString)
        boardList = list(stringRepresentation)
    # move right
    if(((dotIndex + 1) > -1) and ((dotIndex + 1) < len(boardList)) and ((dotIndex % boardSize) != (boardSize - 1))):
        boardList.insert(boardList.index(".") + 1, boardList.pop(boardList.index(".")))
        boardString = "".join(boardList)
        childrenList.append(boardString)
        boardList = list(stringRepresentation)
    # move up
    if(((dotIndex - boardSize) > -1) and ((dotIndex - boardSize) < len(boardList))):
        boardList.insert(boardList.index(".") - int(boardSize), boardList.pop(boardList.index(".")))
        boardList.insert(boardList.index(".") + int(boardSize), boardList.pop(boardList.index(".") + 1))
        boardString = "".join(boardList)
        childrenList.append(boardString)
        boardList = list(stringRepresentation)
    # move down
    if(((dotIndex + boardSize) > -1) and ((dotIndex + boardSize) < len(boardList))):
        boardList.insert(boardList.index(".") + int(boardSize), boardList.pop(boardList.index(".")))
        boardList.insert(boardList.index(".") - int(boardSize), boardList.pop(boardList.index(".") - 1))
        boardString = "".join(boardList)
        childrenList.append(boardString)
        boardList = list(stringRepresentation)
    return childrenList

def findGoal(stringRepresentation):
    boardList = list(stringRepresentation)
    boardList = sorted(boardList)
    boardList.append(boardList.pop(boardList.index(".")))
    goalString = "".join(boardList)
    return goalString

def goalTest(stringRepresentation):
    if stringRepresentation == findGoal(stringRepresentation):
        return True
        
def BFS(startBoard): 
    visited = set()
    fringe = deque()
    fringe.append((startBoard, 0))
    visited.add(startBoard)
    while fringe:
        parent, parentSteps = fringe.popleft()
        if goalTest(parent) == True:
            return parentSteps
        for child in getChildren(parent):
            if child not in visited:
                childSteps = parentSteps + 1
                fringe.append((child, childSteps))
                visited.add(child)
    return None

def kDFS(startBoard, k): 
    visited = set()
    fringe = deque()
    fringe.append((startBoard, 0))
    visited.add(startBoard)
    while fringe:
        parent, parentSteps = fringe.pop()
        if goalTest(parent) == True:
            return parentSteps
        if parentSteps < k:
            for child in getChildren(parent):
                if child not in visited:
                    childSteps = parentSteps + 1
                    fringe.append((child, childSteps))
                    visited.add(child)
    return None

def IDDFS(startBoard):
    maxDepth = 0
    result = None
    while result is None:
        result = kDFS(startBoard, maxDepth)
        maxDepth += 1
    return result

def taxiCabDistance(startBoard):
    taxiCabDistance = 0
    boardSize = len(startBoard) ** 0.5
    for index in range(len(startBoard)):
        if startBoard[index] != ".":
            goalIndex = findGoal(startBoard).index(startBoard[index])
            currentColumn = index % boardSize
            currentRow = int(index/ boardSize)
            goalColumn = goalIndex % boardSize
            goalRow = int(goalIndex/ boardSize)
            taxiCabDistance = taxiCabDistance + abs(currentRow - goalRow) + abs(currentColumn - goalColumn)
    return taxiCabDistance

def aStar(startBoard):
    closed = set()
    fringe = []
    heapq.heapify(fringe)
    heapq.heappush(fringe, (taxiCabDistance(startBoard), 0, startBoard))
    while fringe:
        parentTaxiCab, parentSteps, parent = heapq.heappop(fringe)
        if goalTest(parent) == True:
            return parentSteps
        if parent not in closed:
            closed.add(parent)
            for child in getChildren(parent):
                if child not in closed:
                    childSteps = parentSteps + 1
                    childTaxiCab = childSteps + taxiCabDistance(child)
                    heapq.heappush(fringe, (childTaxiCab, childSteps, child))
    return None

with open(fileName) as f:
    lineList = [line.strip().split() for line in f]
    for lineNum in range(0, len(lineList)):
        searchType = "".join(lineList[lineNum][2])
        stringRepresentation = "".join(lineList[lineNum][1])
        start = time.perf_counter()
        if(parityCheck(stringRepresentation) == False):
            end = time.perf_counter()
            print("Line " + str(lineNum) + ": " + stringRepresentation + ", no solution determined in " + str(end - start) + " seconds")
        else:
            if searchType == "B":
                start = time.perf_counter()
                numMoves = BFS(stringRepresentation)
                end = time.perf_counter()
                print("Line " + str(lineNum) + ": " + stringRepresentation + ", " + "BFS - "+ str(numMoves) + " moves in " + str(end-start) + " seconds")
            elif searchType == "I":
                start = time.perf_counter()
                numMoves = IDDFS(stringRepresentation)
                end = time.perf_counter()
                print("Line " + str(lineNum) + ": " + stringRepresentation + ", " + "ID-DFS - " + str(numMoves) + " moves in " + str(end-start) + " seconds")
            elif searchType == "A":
                start = time.perf_counter()
                numMoves = aStar(stringRepresentation)
                end = time.perf_counter()
                print("Line " + str(lineNum) + ": " + stringRepresentation + ", " + "A* - " + str(numMoves) + " moves in " + str(end-start) + " seconds")
            elif searchType == "!":
                start = time.perf_counter()
                numMoves = BFS(stringRepresentation)
                end = time.perf_counter()
                print("Line " + str(lineNum) + ": " + stringRepresentation + ", " + "BFS - " + str(numMoves) + " moves in " + str(end-start) + " seconds")

                start2 = time.perf_counter()
                numMoves2 = IDDFS(stringRepresentation)
                end2 = time.perf_counter()
                print("Line " + str(lineNum) + ": " + stringRepresentation + ", " + "ID-DFS - "+ str(numMoves) + " moves in " + str(end-start) + " seconds")

                start3 = time.perf_counter()
                numMoves3 = aStar(stringRepresentation)
                end3 = time.perf_counter()
                print("Line " + str(lineNum) + ": " + stringRepresentation + ", " + "A* - " + str(numMoves) + " moves in " + str(end-start) + " seconds")
