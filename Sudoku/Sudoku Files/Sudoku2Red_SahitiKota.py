# Sahiti Kota
# 12/23/2021
import sys
import math
import random
import copy

# N refers to N x N sudoku puzzle 
fileName = sys.argv[1]

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def factors(N):
    factors =  set()
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            factors.add(i)
            factors.add(N//i)
    return factors

def findPuzzleVars(puzzle):
    global N, subblockHeight, subblockWidth, symbolSet
    N = int(len(puzzle) ** 0.5)
    if int(N ** 0.5) == (N ** 0.5):
        subblockHeight = int(N ** 0.5)
        subblockWidth = int(N ** 0.5)
    else:
        subblockHeight = 0
        subblockWidth = 100000
        squareRoot = N ** 0.5
        Nfactors = factors(N)
        for factor in Nfactors:
            if factor < squareRoot and factor > subblockHeight:
                subblockHeight = factor
            if factor > squareRoot and factor < subblockWidth:
                subblockWidth = factor
    symbolSet = []
    if N <= 9:
        for i in range(N):
            symbolSet.append(numbers[i])
    else:
        for i in range(9):
            symbolSet.append(numbers[i])
        for i in range(N - 9):
            symbolSet.append(alphabet[i])

def printPuzzle(puzzle):
    bar = "-" * (N * 2 + 6 + (int(N/ subblockWidth)) - 1 * 2)
    print(bar)
    lineString = "|| "
    h = 0
    while h < N:
        for w in range(N):
            lineString += puzzle[w + (h * N)] + " "
            if w > 0  and w < N - 1 and (w + 1) % (subblockWidth) == 0:
                lineString += "| "
        lineString += "||"
        print(lineString)
        lineString = "|| "
        if (h + 1) % subblockHeight == 0:
            print(bar)
        h += 1 

def getRowConstraintSets():
    rowConstraintSets = [set() for index in range(N)]
    for rSet in range(len(rowConstraintSets)):
        for ind in range(N):
            rowConstraintSets[rSet].add(ind + (N * rSet))
    return rowConstraintSets

def getSubblockConstraintSets():
    subblockConstraintSets = {}
    for row in range(N):
        for column in range(N):
            block = (row // subblockHeight, column // subblockWidth)
            if block not in subblockConstraintSets:
                subblockConstraintSets[block] = set()
            subblockConstraintSets[block].add((row * N + column))
    return subblockConstraintSets.values()

def getColumnConstraintSets():
    columnConstraintSets = [set() for index in range(N)]
    for cSet in range(len(columnConstraintSets)):
        for ind in range(cSet, N ** 2, N):
            columnConstraintSets[cSet].add(ind)
    return columnConstraintSets

def findRowConstraintSet(index):
    rowConstraint = set()
    rowNumber = int(index/ N)
    for ind in range(N):
        rowConstraint.add(ind + (N * rowNumber))
    return rowConstraint

def findColumnConstraintSet(index):
    columnConstraint = set()
    columnNumber = int(index % N)
    for ind in range(columnNumber, N ** 2, N):
        columnConstraint.add(ind)
    return columnConstraint

def findSubblockConstraintSet(index):
    subblockConstraint = set()
    rowNumber = int(index/ N)
    columnNumber = int(index % N)
    groupRowNumber = int(rowNumber/ subblockHeight)
    groupColumnNumber = int(columnNumber/ subblockWidth)
    for row in range(N):
        for column in range(N):
            if int(row/ subblockHeight) == groupRowNumber and int(column/ subblockWidth) == groupColumnNumber:
                subblockConstraint.add(row * N + column)
    return subblockConstraint

def findNeighborSets(puzzle):
    global nS
    nS = [[] for index in range(N ** 2)]
    for index in range(N ** 2):
        nS[index] = list(findRowConstraintSet(index)) + list(findColumnConstraintSet(index)) + list(findSubblockConstraintSet(index))
        nS[index] = sorted(list(dict.fromkeys(nS[index])))
        nS[index].remove(index)

def countSymbolSet(puzzle):
    symbolSet = []
    stringSet = {x for x in list(puzzle)}
    for char in stringSet:
        symbolSet.append((char, puzzle.count(char)))
    return symbolSet

def puzzleBuildHelper(state, var):
    constraintList = nS[var]
    notPossible = []
    possible = []
    for index in constraintList:
        if len(state[index]) == 1 and state[index] != '.':
            notPossible.append(state[index])
    for value in symbolSet:
        if value not in notPossible:
            possible.append(value)
    return(sorted(possible))

def getSortedValues(puzzle, var):
    return (list(puzzle[var]))

def goalTest(state):
    for item in state:
        if len(item) > 1:
            return False
    return True

def createStructure(puzzle):
    possibleValuesList = []
    for index in range(len(puzzle)):
        string = ""
        if puzzle[index] == ".":
            for item in puzzleBuildHelper(puzzle, int(index)):
                string += item
        else:
            string += puzzle[index]
        possibleValuesList.append(string)
    return possibleValuesList

def getMostConstrainedVar(board):
    min = 1000000
    minList = []
    for index in range(len(board)):
        if len(board[index]) < min and len(board[index]) > 1:
            min = len(board[index])
            minList = [index]
        elif len(board[index]) == min:
            minList.append(index)
    return random.choice(minList)

def forwardLooking(board, nS):
    solvedIndices = []
    visited = set()
    newBoard =  copy.copy(board)
    for index in range(len(board)):
        if len(board[index]) == 1:
            solvedIndices.append(index)
            visited.add(index)
    while solvedIndices:
        index = solvedIndices.pop()
        value = newBoard[index]
        for neighbor in nS[index]:
            if value in newBoard[neighbor]:
                newBoard[neighbor] = newBoard[neighbor].replace(value, '')
            if len(newBoard[neighbor]) == 1 and neighbor not in visited:
                solvedIndices.append(neighbor)
                visited.add(neighbor)
            elif len(newBoard[neighbor]) == 0:
                return None
    return newBoard

def constraintPropogation(state):
    changeMade = False
    rowSets = getRowConstraintSets()
    columnSets = getColumnConstraintSets()
    subblockSets = getSubblockConstraintSets()
    allSets = rowSets + columnSets
    for set in subblockSets:
        allSets.append(set)
    for constraintSet in allSets:
        for possibleValue in symbolSet:
            indicesValue = []
            for index in constraintSet:
                if possibleValue in state[index]:
                    indicesValue.append(index)
            if len(indicesValue) == 1:
                if len(state[indicesValue[0]]) > 1:
                    # changing correctly
                    state[indicesValue[0]] = possibleValue
    return state

def cspBacktrackingWithForwardLooking(state, nS):
    if goalTest(state):
        return state
    var = getMostConstrainedVar(state)
    for val in getSortedValues(state, var):
        newState = copy.copy(state)
        newState[var] = str(val)
        checkedState = forwardLooking(newState, nS)
        if checkedState is not None:
            checkedState = constraintPropogation(checkedState)
            result = cspBacktrackingWithForwardLooking(checkedState, nS)
            if result is not None:
                return result
    return None

with open(fileName) as f:
    lineList = [line.strip().split() for line in f]
    for lineNum in range(0, len(lineList)):
        puzzle = "".join(lineList[lineNum])
        findPuzzleVars(puzzle)
        findNeighborSets(puzzle)
        string = ""
        for item in cspBacktrackingWithForwardLooking(createStructure(puzzle), nS):
            string += item
        print(string)