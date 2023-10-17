# Sahiti Kota
# 12/22/2021
import sys
import math

# N refers to N x N sudoku puzzle 
fileName = 'puzzles_1_standard_easy.txt' #sys.argv[1]

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
    neighborSets = [[] for index in range(N ** 2)]
    for index in range(N ** 2):
        neighborSets[index] = list(findRowConstraintSet(index)) + list(findColumnConstraintSet(index)) + list(findSubblockConstraintSet(index))
        neighborSets[index] = sorted(list(dict.fromkeys(neighborSets[index])))
        neighborSets[index].remove(index)
    return neighborSets

def countSymbolSet(puzzle):
    symbolSet = []
    stringSet = {x for x in list(puzzle)}
    for char in stringSet:
        symbolSet.append((char, puzzle.count(char)))
    return symbolSet

# backtracking
def getNextUnassignedVar(state):
    for char in range(len(state)):
        if state[char] == ".":
            return char

def getSortedValues(state, var, nS):
    constraintList = nS[var]
    notPossible = []
    possible = []
    for index in constraintList:
        if state[index] != '.':
            notPossible.append(state[index])
    for value in symbolSet:
        if value not in notPossible:
            possible.append(value)
    return(sorted(possible))

def goalTest(state):
    for char in state:
        if char == '.':
            return False
    return True

def cspBacktracking(state, nS):
    if goalTest(state):
        return state
    var = getNextUnassignedVar(state)
    for val in getSortedValues(state, var, nS):
        # create newState by assigning val to var
        newState = state[:var] + str(val) + state[var + 1:]
        result = cspBacktracking(newState, nS)
        if result is not None:
            return result
    return None

with open(fileName) as f:
    lineList = [line.strip().split() for line in f]
    for lineNum in range(0, len(lineList)):
        puzzle = "".join(lineList[lineNum])
        findPuzzleVars(puzzle)
        neighborSets = findNeighborSets(puzzle)
        print(cspBacktracking(puzzle, neighborSets))