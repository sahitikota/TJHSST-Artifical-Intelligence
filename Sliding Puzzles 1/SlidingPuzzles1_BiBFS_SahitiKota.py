# Sahiti Kota
# 12/20/2021
from collections import deque
import sys
import time

fileName = sys.argv[1]

def BFS(startBoard): 
    visited = set()
    fringe = deque()
    fringe.append((startBoard, 0, [startBoard]))
    visited.add(startBoard)
    while fringe:
        parent, parentSteps, parentPath = fringe.popleft()
        if goalTest(parent) == True:
            return parentSteps
        for child in getChildren(parent):
            if child not in visited:
                childPath = parentPath.copy()
                childPath.append(child)
                childSteps = parentSteps + 1
                fringe.append((child, childSteps, childPath))
                visited.add(child)
    return None

def BiBFS(startBoard):
    visitedStart = set()
    fringeStart = deque()
    visitedTarget = set()
    visitedStartSteps = {}
    visitedTargetSteps = {}
    fringeTarget = deque()
    totalStart = deque()
    totalTarget = deque
    targetBoard = findGoal(startBoard)
    visitedStart.add(startBoard)
    fringeStart.append((startBoard, 0, [startBoard]))
    visitedTarget.add(targetBoard)
    fringeTarget.append((targetBoard, 0, [targetBoard]))
    while fringeStart and fringeTarget:
        if fringeStart:
            parent, parentSteps, parentPath = fringeStart.popleft()
            for child in getChildren(parent):
                if child in visitedTarget:
                    childPath = parentPath.copy()
                    childPath.append(child)
                    childSteps = parentSteps + 1
                    if len(visitedTargetSteps) > 0:
                        return childSteps + visitedTargetSteps[child][0]
                    else:
                        return childSteps
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
                    return childSteps + visitedStartSteps[child][0]
                elif child not in visitedTarget:
                    childPath = parentPath.copy()
                    childPath.append(child)
                    childSteps = parentSteps + 1
                    fringeTarget.append((child, childSteps, childPath))
                    visitedTarget.add(child)
                    visitedTargetSteps[child] = (childSteps, childPath)
    return None

def printPuzzle(size, stringRepresentation):
    toPrint = ""
    for index in range (0, len(stringRepresentation)):
        if index % size != 0:
            toPrint += stringRepresentation[index] + " "
        elif index % size == 0:
            toPrint += '\n'
            toPrint += stringRepresentation[index] + " "
    return toPrint

def findGoal(stringRepresentation):
    boardList = list(stringRepresentation)
    boardList = sorted(boardList)
    boardList.append(boardList.pop(boardList.index(".")))
    goalString = "".join(boardList)
    return goalString

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

def goalTest(stringRepresentation):
    if stringRepresentation == findGoal(stringRepresentation):
        return True

with open(fileName) as f:
    lineList = [line.strip().split() for line in f]
    for lineNum in range(0, len(lineList)):
        stringRepresentation = "".join(lineList[lineNum])
        start = time.perf_counter()
        numMoves = BFS(stringRepresentation)
        end = time.perf_counter()
        print("Line", lineNum, ":", stringRepresentation, ",", numMoves, "moves found in %s" % str(end-start), "seconds")
        start = time.perf_counter()
        numMoves = BiBFS(stringRepresentation)
        end = time.perf_counter()
        print("Line", lineNum, ":", stringRepresentation, ",", numMoves, "moves found in %s" % str(end-start), "seconds")