# Sahiti Kota
# 10/18/2021

import time
import random

def goalTest(state):
    if None in state:
        return False
    return True

def getNextUnassignedVar(state):
    '''midpoint = int((len(state)/2))
    for i in range(midpoint, -1, -1):
        if i < midpoint:
            if state[i] == None:
                return i
            elif state[len(state) - i - 1] == None:
                return len(state) - i - 1  
        else:
            if state[i] == None:
                return i'''
    notAssigned = []
    for i in range(len(state)):
        if state[i] == None:
            notAssigned.append(i)
    return random.choice(notAssigned)

def getSortedValues(state, var):
    values = []
    invalidValues = []
    # var is the row
    # iterating through the columns
    for column in range(len(state)):
        if column in state:
            invalidValues.append(column)
        else:
            for row in range(len(state)):
                if state[row] != None:
                    if abs(var - row) == abs(column - state[row]):
                        invalidValues.append(column)
    for value in range(len(state)):
        if value not in invalidValues:
            values.append(value)
    values = sorted(values)
    return values

def cspBacktracking(state):
    if goalTest(state):
        return state
    var = getNextUnassignedVar(state)
    for val in getSortedValues(state, var):
        # create newState by assigning val to var
        newState = state.copy()
        newState[var] = val
        result = cspBacktracking(newState)
        if result is not None:
            return result
    return None

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
overallStart = time.perf_counter()
state = [None] * 30
print(cspBacktracking(state))
state = [None] * 31
print(cspBacktracking(state))
overallEnd = time.perf_counter()
print("Time taken was", overallEnd - overallStart, "seconds")
