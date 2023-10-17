# Sahiti Kota
# 11/02/2021

import random
import time
# use random to return random column value and problem row

def findNumberOfConflicts(state):
    conflictsCount = 0
    conflictsList = []
    for row1 in range(len(state)):
        for row2 in range(row1 + 1, len(state)):
            if (abs(row1 - row2) == abs(state[row1] - state[row2])) or state[row1] == state[row2]:
                conflictsList.append((row1, row2))
                conflictsCount += 1
    return conflictsCount, conflictsList

def getProblemRow(state):
    '''numberConflictsList = []
    maxConflictsList = []
    for row in state:
        numberConflictsList.append(findNumberOfConflicts(state, row))
    maxConflicts = max(numberConflictsList)
    for row in range(len(numberConflictsList)):
        if numberConflictsList[row] == maxConflicts:
            maxConflictsList.append(row)
    return random.choice(maxConflictsList)'''
    conflictsCount, conflictsList = findNumberOfConflicts(state)
    # print(conflictsList)
    conflictsCountList = [0] * len(state)
    for conflict in range(len(conflictsList)):
        # adding conflict to both rows involved in conflict
        firstConflictRow = conflictsList[conflict][0]
        secondConflictRow = conflictsList[conflict][1]
        conflictsCountList[firstConflictRow] += 1
        conflictsCountList[secondConflictRow] += 1
    maxConflicts = max(conflictsCountList)
    maxConflictsList = []
    # i think the issue might be here, not adding all of the rows that have the same number of conflicts as max
    for i in range(len(conflictsCountList)):
        if(conflictsCountList[i] == maxConflicts):
            maxConflictsList.append(i)
    # print("m", maxConflicts, maxConflictsList)
    return random.choice(maxConflictsList)

def getLeastAttackingColumn(state, problemRow):
    '''numberConflictsList = []
    minConflictsList = []
    for column in range(len(state)):
        state[problemRow] = column
        numberConflictsList.append(findNumberOfConflicts(state, problemRow))
    minConflicts = min(numberConflictsList)
    for row in range(len(numberConflictsList)):
        if numberConflictsList[row] == minConflicts:
            minConflictsList.append(row)
    return random.choice(minConflictsList)'''
    conflictsCountList = []
    for possibleColumn in range(len(state)):
        conflictCount = 0
        for j in range(len(state)):
            if possibleColumn == state[j] or abs(possibleColumn - state[j]) == abs(problemRow - j):
                conflictCount += 1
        conflictsCountList.append(conflictCount)
    minConflicts = min(conflictsCountList)
    minConflictsList = []
    for k in range(len(conflictsCountList)):
        if(conflictsCountList[k] == minConflicts):
            minConflictsList.append(k)
    return random.choice(minConflictsList)

# number of conflicts isn't changing
def cspIncrementalRepair(state):
    while findNumberOfConflicts(state)[0] != 0:
        problemRow = getProblemRow(state)
        bestColumn = getLeastAttackingColumn(state, problemRow)
        state[problemRow] = bestColumn
        print("Number of Conflicts:", findNumberOfConflicts(state)[0])
        print("State;", state)
    return state

def testSolution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    return True

state =  [None] * 31
possiblePlacements = [i for i in range(len(state))]
for i in range(len(state)):
    value = random.choice(possiblePlacements)
    state[i] = value
    possiblePlacements.remove(value)

start = time.perf_counter()
print(state)
print("Final State:", cspIncrementalRepair(state))
print(testSolution(cspIncrementalRepair(state)))

state2 =  [None] * 33
possiblePlacements = [i for i in range(len(state2))]
for i in range(len(state2)):
    value = random.choice(possiblePlacements)
    state2[i] = value
    possiblePlacements.remove(value)

print(state2)
print("Final State:", cspIncrementalRepair(state2))
print(testSolution(cspIncrementalRepair(state2)))
end = time.perf_counter()
print('Time taken:', end-start, 'seconds')