# Sahiti Kota
# 02/21/2022
import sys

testFile = sys.argv[2]

# printing DFA to console
def printDFA(dfa, chars, numStates, finalStates):
    print("*     ", end = "")
    for char in chars:
        print(char + "     ", end = "")
    print(" ")
    for state in range(numStates):
        print(state, "    ", end = "")
        for char in chars:
            print(end = "")
            if char in dfa[state].keys():
                print(dfa[state][char], "    ", end = "")
            else:
                print('_', "    ", end = "")
        print("")
    print("Final nodes:", finalStates)

# testing DFA test cases
def testString(test, dfa, finalStates):
    state = 0
    if test == '':
        if test in dfa[state].keys():
            state = dfa[state][test]
        if state in finalStates:
            return True
        elif state not in finalStates:
            return False
    else:
        for character in range(len(test)):
            if test[character] in dfa[state].keys():
                state = dfa[state][test[character]]
            elif test[character] not in dfa[state].keys():
                return False
            if character == len(test) - 1 and state in finalStates:
                return True
            elif character == len(test) - 1 and state not in finalStates:
                return False

try:
    # written DFAs
    dfaNum = int(sys.argv[1])

    dfa1 = {0: {'a': 1, '': 0},1: {'a': 2}, 2: {'b': 3}, 3: {}}
    dfa2 = {0: {'0': 0, '1': 1, '2': 0, '': 0}, 1: {'0': 0, '1': 1, '2': 0}}
    dfa3 = {0: {'a': 0, 'b': 1, 'c': 0, '': 0}, 1: {'a': 1, 'b': 1, 'c': 1}}
    dfa4 = {0: {'0': 1, '1': 2, '': 2}, 1: {'0': 2, '1': 1}, 2: {'0': 1, '1': 2}}
    dfa5 = {0: {'0': 1, '1': 3, '': 3, }, 1: {'0': 0, '1': 2}, 2: {'0': 3, '1': 1}, 3: {'0': 2, '1': 0, '': 3}}
    dfa6 = {0: {'a': 1, 'b': 0, 'c': 0, '': 0}, 1: {'a': 1, 'b': 2, 'c': 0}, 2: {'a': 1, 'b': 0, 'c': 3}, 3: {'a': 3, 'b': 3, 'c': 3}}
    dfa7 = {0: {'0': 0, '1': 1, '': 0}, 1: {'0': 2, '1': 0}, 2: {'0': 2, '1': 3}, 3: {'0': 2, '1': 4}, 4: {'0': 4, '1': 4}}
    dfaList = [(dfa1, ['a','b'], 4, [3]), (dfa2, ['0', '1', '2'], 2, [1]), (dfa3, ['a', 'b', 'c'], 2, [1]), (dfa4, ['0', '1'], 3, [2]), (dfa5, ['0', '1'], 3, [0]), (dfa6, ['a', 'b', 'c'], 4, [0, 1, 2]), (dfa7, ['0', '1'], 5, [4])]
    dfa = dfaList[dfaNum - 1][0]

    printDFA(dfaList[dfaNum - 1][0], dfaList[dfaNum - 1][1], dfaList[dfaNum - 1][2], dfaList[dfaNum - 1][3])
    with open(testFile) as f:
        for test in f:
            print(testString(test.strip(), dfa, dfaList[dfaNum - 1][3]), test.strip())

except ValueError:
    specFile = sys.argv[1]
    f = open(specFile, "r")
    splitSpec = f.read().split('\n\n')
    size = splitSpec[0].split('\n')
    chars = [x for x in size[0]]
    numStates = int(size[1])
    finalStates = [int(x) for x in size[2] if x.isdigit()]

    dfa = {}

    splitSpec = splitSpec[1:]
    for connection in splitSpec:
        startState = connection.split()[0]
        connList = connection.split('\n')
        connList.pop(0)
        if len(connList) == 0:
            dfa[int(startState)] = {}
        else:
            transDict = {}
            for item in connList:
                transition, finalState = item.split(' ')
                transDict[transition] = int(finalState)
                dfa[int(startState)] = transDict

    with open(testFile) as f:
        for test in f:
            print(testString(test.strip(), dfa, finalStates), test.strip())