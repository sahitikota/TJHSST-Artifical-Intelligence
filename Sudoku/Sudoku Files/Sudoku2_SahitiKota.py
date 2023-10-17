# Sahiti Kota
# 11/14/2021
from copy import deepcopy
import sys

# DOES NOT WORK -- REFER TO SUDOKU 2 RED FOR CORRECT FORWARD LOOKING
fileName = 'puzzles_3_standard_medium.txt' #sys.argv[1]

rowOneConstraintSet = set(range(0, 9))
rowTwoConstraintSet = set(range(9, 18))
rowThreeConstraintSet = set(range(18, 27))
rowFourConstraintSet = set(range(27, 36))
rowFiveConstraintSet = set(range(36, 45))
rowSixConstraintSet = set(range(45, 54))
rowSevenConstraintSet = set(range(54, 63))
rowEightConstraintSet = set(range(63, 71))
rowNineConstraintSet = set(range(72, 81))

columnOneConstraintSet = set(range(0, 73, 9))
columnTwoConstraintSet = set(range(1, 74, 9))
columnThreeConstraintSet = set(range(2, 75, 9))
columnFourConstraintSet = set(range(3, 76, 9))
columnFiveConstraintSet = set(range(4, 77, 9))
columnSixConstraintSet = set(range(5, 78, 9))
columnSevenConstraintSet = set(range(6, 79, 9))
columnEightConstraintSet = set(range(7, 80, 9))
columnNineConstraintSet = set(range(8, 81, 9))

subBlockOneConstraintSet = {*set(range(0, 3)), *set(range(9, 12)), *set(range(18, 21))}
subBlockTwoConstraintSet = {*set(range(3, 6)), *set(range(12, 15)), *set(range(21, 24))}
subBlockThreeConstraintSet = {*set(range(6, 9)), *set(range(15, 18)), *set(range(24, 27))}
subBlockFourConstraintSet = {*set(range(27, 30)), *set(range(36, 39)), *set(range(45, 48))}
subBlockFiveConstraintSet = {*set(range(30, 33)), *set(range(39, 42)), *set(range(48, 51))}
subBlockSixConstraintSet = {*set(range(33, 36)), *set(range(42, 45)), *set(range(51, 54))}
subBlockSevenConstraintSet = {*set(range(54, 57)), *set(range(63, 66)), *set(range(72, 75))}
subBlockEightConstraintSet = {*set(range(57, 60)), *set(range(66, 69)), *set(range(75, 78))}
subBlockNineConstraintSet = {*set(range(60, 63)), *set(range(69, 72)), *set(range(78, 80))}

rowConstraintSets = [rowOneConstraintSet, rowTwoConstraintSet, rowThreeConstraintSet, rowFourConstraintSet, rowFiveConstraintSet, rowSixConstraintSet, rowSevenConstraintSet, rowEightConstraintSet, rowNineConstraintSet]
columnConstraintSets = [columnOneConstraintSet, columnTwoConstraintSet, columnThreeConstraintSet, columnFourConstraintSet, columnFiveConstraintSet, columnSixConstraintSet, columnSevenConstraintSet, columnEightConstraintSet, columnNineConstraintSet]
subBlockConstraintSets =[subBlockOneConstraintSet, subBlockTwoConstraintSet, subBlockThreeConstraintSet, subBlockFourConstraintSet, subBlockFiveConstraintSet, subBlockSixConstraintSet, subBlockSevenConstraintSet, subBlockEightConstraintSet, subBlockNineConstraintSet]

neighborSetLists = [[] for index in range(81)]

for set in rowConstraintSets:
    for index in range(81):
        if index in set:
            neighborSetLists[index] = list(set)

for index in range(81):
    for set in columnConstraintSets:
        if index in set:
            neighborSetLists[index] += list(set)

for set in subBlockConstraintSets:
    for index in range(81):
        if index in set: 
            neighborSetLists[index] += list(set)
            neighborSetLists[index] = sorted(list(dict.fromkeys(neighborSetLists[index])))
            neighborSetLists[index].remove(index)

puzzleList = open(fileName).read().split()

def printPuzzle(string):
    print("---------------------------")
    print("||", string[0], string[1], string[2], "|", string[3], string[4], string[5], "|", string[6], string[7], string[8], "||")
    print("||", string[9], string[10], string[11], "|", string[12], string[13], string[14], "|", string[15], string[16], string[17], "||")
    print("||", string[18], string[19], string[20], "|", string[21], string[22], string[23], "|", string[24], string[25], string[26], "||")
    print("---------------------------")
    print("||", string[27], string[28], string[29], "|", string[30], string[31], string[32], "|", string[33], string[34], string[35], "||")
    print("||", string[36], string[37], string[38], "|", string[39], string[40], string[41], "|", string[42], string[43], string[44], "||")
    print("||", string[45], string[46], string[47], "|", string[48], string[49], string[50], "|", string[51], string[52], string[53], "||")
    print("---------------------------")
    print("||", string[54], string[55], string[56], "|", string[57], string[58], string[59], "|", string[60], string[61], string[62], "||")
    print("||", string[63], string[64], string[65], "|", string[66], string[67], string[68], "|", string[69], string[70], string[71], "||")
    print("||", string[72], string[73], string[74], "|", string[75], string[76], string[77], "|", string[78], string[79], string[80], "||")
    print("---------------------------")
    print("")

def findSymbolSet(string):
    symbolSet = []
    stringSet = {x for x in list(string)}
    for char in stringSet:
        symbolSet.append((char, string.count(char)))
    return symbolSet

def getSortedValues(state, var):
    constraintList = neighborSetLists[var]
    notPossible = []
    possible = []
    for index in constraintList:
        if state[index] != '.':
            notPossible.append(int(state[index]))
    for value in range(1, 10):
        if value not in notPossible:
            possible.append(value)
    return (sorted(possible))

def goalTest(state):
    for item in state.items():
        key, value = item
        if len(value) > 1:
            return False
    return True

def createBackingStructure(puzzle):
    range81 = [i for i in range(81)]
    possibleValuesDictionary = dict(zip(range81, [None]*len(range81)))
    for index in range(len(puzzle)):
        if puzzle[index] == ".":
            possibleValuesDictionary[index] = getSortedValues(puzzle, int(index))
        else:
            possibleValuesDictionary[index] = [int(puzzle[index])]
    return possibleValuesDictionary

def getMostConstrainedVar(possibleValuesDictionary):
    min = 1000000
    minKey = None
    for item in possibleValuesDictionary.items():
        key, value = item
        if len(value) < min and len(value) > 1:
            min = len(value)
            minKey = key
    return minKey

def forwardLooking(possibleValuesDictionary):
    solvedList = []
    completelyDone = []
    for item in possibleValuesDictionary.items():
        key, value = item
        if len(value) == 1:
            solvedList.append((key, value))
            completelyDone.append(key)
    while len(solvedList) != 0:
        key, value = solvedList.pop()
        neighborList = neighborSetLists[key]
        for index in neighborList:
            if index in completelyDone:
                continue
            possibleValues = possibleValuesDictionary[index]
            if value[0] in possibleValues:
                possibleValues.remove(value[0])
                possibleValuesDictionary[index] = possibleValues
            if len(possibleValues) == 1:
                solvedList.append((index, possibleValues))
                completelyDone.append(index)
            elif len(possibleValues) == 0:
                return None
    return possibleValuesDictionary

def cspBackTrackingWithForwardTracking(state):
    if goalTest(state):
        return state
    var = getMostConstrainedVar(state)
    for val in state[var]:
        newState = deepcopy(state)
        newState[var] = [val]
        checkedState = forwardLooking(newState)
        if checkedState is not None:
            result = cspBackTrackingWithForwardTracking(checkedState)
            if result is not None:
                return result
    return None

for puzzle in puzzleList:
    state = createBackingStructure(puzzle)
    final = ""
    for item in cspBackTrackingWithForwardTracking(state).items():
        key, value = item
        final += str(value)[1:-1]
    printPuzzle(final)

# print(createBackingStructure("....8.4....2....1..6.......59....1.....6.2.......7.......5...6.4..1.....3...4...."))
