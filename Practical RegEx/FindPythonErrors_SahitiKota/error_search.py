# Sahiti Kota
# 02/22/2022
import sys
import re

errorFile = 'error_example.py' # sys.argv[1]

digitStartsVar = re.compile(r"\d+\w* *=")
methodCall = re.compile(r"\w*\(.*\)\w*")
missingColons = [re.compile(r"\w*for\w*"), re.compile(r"\w*if\w*"), re.compile(r"\w*else\w*"), re.compile(r"\w*elif\w*"), re.compile(r"\w*while\w*")]
globalVariables = re.compile(r" {4}[A-Z]+")
wrongEqual = re.compile(r"\s*(while|for|if|elif|else).*=.*:")

lineNum = 1
lineNums = []

# variable that starts with a digit
with open(errorFile) as f:
    for line in f:
        for result in digitStartsVar.finditer(line):
            start, end = result.span()
            lineNums.append(lineNum)
        lineNum += 1
print("Found a variable starting with a digit on line(s):", lineNums)

lineNum = 1
reviewLineNum = 1
lineNums = []
resultsCharacters = []
wrong = []
# method call before defined variable
with open(errorFile) as f:
    for line in f:
        call = ""
        for result in methodCall.finditer(line):
            start, end = result.span()
            for char in range(start, end):
                call += line[char]
            varName = call.split("(")[1]
            varName = varName[0:len(varName) - 1]
            lineNums.append(lineNum)
            resultsCharacters.append((varName, lineNum))
        lineNum += 1
    if len(resultsCharacters) > 0:
        for varName, lineNum in resultsCharacters:
            mod = "^" + varName + " *= *"
            varDef = re.compile(mod)
            # print(varDef)
            with open(errorFile) as f:
                for line in f:
                    for result in varDef.finditer(line):
                        startVar, endVar = result.span()
                        if reviewLineNum > lineNum:
                            wrong.append(lineNum)
                    reviewLineNum += 1
for num in wrong:
    lineNums.remove(num)
print("Found a method call on a variable not defined on line(s):", lineNums)

reviewLineNum = 1
lineNums = []
resultsCharacters = []
wrong = set()
lineNum = 1
# find missing colons
with open(errorFile) as f:
    for line in f:
        call = ""
        for regEx in missingColons:
            for result in regEx.finditer(line):
                start, end = result.span()
                for char in range(start, end):
                    call += line[char]
                varName = call.split(".")[0]
                lineNums.append(lineNum)
                resultsCharacters.append((varName, lineNum))
        lineNum += 1
    if len(resultsCharacters) > 0:
        for varName, lineNum in resultsCharacters:
            mod = ".*" + varName + ".*:.*"
            varDef = re.compile(mod)
            l = 1
            with open(errorFile) as f:
                for line in f:
                    for result in varDef.finditer(line):
                        start, end = result.span()
                        if end - start > 0:
                            wrong.add(l)
                    l += 1
for num in wrong:
    lineNums.remove(num)
print("Found a missing colon on line(s):",lineNums)

lineNums = []
resultsCharacters = []
lineNum = 1
# modifying global variables in a loop
with open(errorFile) as f:
    for line in f:
        for result in globalVariables.finditer(line):
            start, end = result.span()
            lineNums.append(lineNum)
        lineNum += 1
print("Found a global variable edited in a loop on line(s):",lineNums)

lineNums = []
resultsCharacters = []
lineNum = 1
# modifying global variables in a loop
with open(errorFile) as f:
    for line in f:
        for result in wrongEqual.finditer(line):
            start, end = result.span()
            lineNums.append(lineNum)
        lineNum += 1
print("Found = used instead of == on line(s):",lineNums)
        