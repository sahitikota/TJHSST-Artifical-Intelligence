# Sahiti Kota
# 02/15/2022
import sys
import re

textFile = sys.argv[1]
stringLine = ""

with open(textFile) as f:
    for line in f:
        stringLine += '\n' + line.lower() + '\n'

# Regular Expression 1
word  = ""
all = []
min  = []
minLength = 100000000
regularExpression = re.compile(r"\b(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)\w+\b")

for result in regularExpression.finditer(stringLine):
    start, end = result.span()
    for char in range(start, end):
        word += stringLine[char]
    if len(word) < minLength:
        minLength = len(word)
    all.append(word)
    word = ""
for word in all:
    if len(word) == minLength:
        min.append(word)
print("#1", regularExpression)
print(len(min), "total matches")
for word in min[0:5]:
    print(word)
print('\n')

# Regular Expression 2
word  = ""
all = []
max = []
maxLength = 0
regularExpression = re.compile(r"\b[^aeiou \n]*[aeiou][^aeiou \n]*[aeiou][^aeiou \n]*[aeiou][^aeiou \n]*[aeiou][^aeiou \n]*[aeiou][^aeiou \n]*\b")

for result in regularExpression.finditer(stringLine):
    start, end = result.span()
    for char in range(start, end):
        word += stringLine[char]
    if len(word) > maxLength:
        maxLength = len(word)
    all.append(word)
    word = ""
for word in all:
    if len(word) == maxLength:
        max.append(word)
print("#2", regularExpression)
print(len(max), "total matches")
for word in max[0:5]:
    print(word)
print('\n')

# Regular Expression 3
word  = ""
all = []
max = []
maxLength = 0
regularExpression = re.compile(r"\b(\w)(?!\w*\1+\w*\1\b)\w*\1\b")

for result in regularExpression.finditer(stringLine):
    start, end = result.span()
    for char in range(start, end):
        word += stringLine[char]
    if len(word) > maxLength:
        maxLength = len(word)
    all.append(word)
    word = ""
for word in all:
    if len(word) == maxLength:
        max.append(word)
print("#3", regularExpression)
print(len(max), "total matches")
for word in max[0:5]:
    print(word)
print('\n')

# Regular Expression 4
word  = ""
all = []
regularExpression = re.compile(r"\b(\w)\w\1\b|\b(\w)(\w)\w?\3\2\b|\b(\w)(\w)(\w)\w*\6\5\4\b")

for result in regularExpression.finditer(stringLine):
    start, end = result.span()
    for char in range(start, end):
        word += stringLine[char]
    all.append(word)
    word = ""
print("#4", regularExpression)
print(len(all), "total matches")
for word in all[0:5]:
    print(word)
print('\n')

# Regular Expression 5
word  = ""
all = []
regularExpression = re.compile(r"\b(?!\w*b\w+t\w*)(?!\w*t\w+b\w*)(?=\w*tb)(?!\w*b\w+t\w*)(?!\w*t\w+b\w*)\w*\b|\b(?!\w*b\w+t\w*)(?!\w*t\w+b\w*)(?=\w*bt)(?!\w*b\w+t\w*)(?!\w*t\w+b\w*)\w*\b|\b(?!\w*b\w+t\w*)(?!\w*t\w+b\w*)(?=\w*tb)(?!\w*t\w+b\w*)(?!\w*t\w+b\w*)\w*\b|\b(?!\w*b\w+t\w*)(?!\w*t\w+b\w*)(?=\w*bt)(?!\w*t\w+b\w*)(?!\w*t\w+b\w*)\w*\b")

for result in regularExpression.finditer(stringLine):
    start, end = result.span()
    for char in range(start, end):
        word += stringLine[char]
    all.append(word)
    word = ""
print("#5", regularExpression)
print(len(all), "total matches")
for word in all[0:5]:
    print(word)
print('\n')

# Regular Expression 6
word  = ""
all = []
maxLength = 0
max = []
maxWords = []
regExs = []
regularExpression = re.compile(r"(\w)\1+")

for result in regularExpression.finditer(stringLine):
    start, end = result.span()
    for char in range(start, end):
        word += stringLine[char]
    if len(word) > maxLength:
        maxLength = len(word)
    all.append(word)
    word = ""
for word in all:
    if len(word) == maxLength:
        max.append(word)
for word in max:
    mod = '\\b.*' + word + '.*\\b'
    rE = re.compile(mod)
    regExs.append(rE)
    for result in rE.finditer(stringLine):
        w = ""
        start, end = result.span()
        for char in range(start, end):
            w += stringLine[char]
        maxWords.append(w)
print("#6", regularExpression)
for item in regExs:
    print(item)
print(len(max), "total matches")
for word in maxWords[0:5]:
    print(word)
print('\n')

# Regular Expression 7
word  = ""
all = []
max = []
repeatCount = 1
matches = True
while matches == True:
    matches = False
    rE = "(\w)+(\w*\\1\w*){" + str(repeatCount) + ",}"
    regularExpression = re.compile(rE)
    for result in regularExpression.finditer(stringLine):
        matches = True
        start, end = result.span()
        for char in range(start, end):
            word += stringLine[char]
        all.append((repeatCount, word))
        word = ""
    repeatCount += 1
for count, word in all:
    if count == repeatCount - 2:
        max.append(word)
print("#7", "re.compile('(\\w)+(\\w*\\1\\w*){" + str(1) + ",}')")
r = 2
while r < repeatCount - 1:
    print("re.compile('(\\w)+(\\w*\\1\\w*){" + str(r) + ",}')")
    r += 1
print(len(max), "total matches")
for word in max[0:5]:
    print(word)
print('\n')

#Regular Expression 8
word  = ""
all = []
max = []
repeatCount = 1
matches = True
while matches == True:
    matches = False
    rE = "\\b\w*(\w\w)+(\w*\\1\w*){" + str(repeatCount) + ",}\\b"
    regularExpression = re.compile(rE)
    for result in regularExpression.finditer(stringLine):
        matches = True
        start, end = result.span()
        for char in range(start, end):
            word += stringLine[char]
        all.append((repeatCount, word))
        word = ""
    repeatCount += 1
for count, word in all:
    if count == repeatCount - 2:
        max.append(word)
print("#8", "re.compile('\\b\w*(\w\w)+(\w*\\1\w*){" + str(1) + ",}\\b')")
r = 2
while r < repeatCount - 1:
    print("re.compile('\\b\w*(\w\w)+(\w*\\1\w*){" + str(r) + ",}\\b')")
    r += 1
print(len(max), "total matches")
for word in max[0:5]:
    print(word)
print('\n')

# Regular Expression 9
word  = ""
all = []
max = []
repeatCount = 1
matches = True
while matches == True:
    matches = False
    rE = "\\b([aeiou]*[^ \\naeiou][aeiou]*){" + str(repeatCount) + ",}\\b"
    regularExpression = re.compile(rE)
    for result in regularExpression.finditer(stringLine):
        matches = True
        start, end = result.span()
        for char in range(start, end):
            word += stringLine[char]
        all.append((repeatCount, word))
        word = ""
    repeatCount += 1
for count, word in all:
    if count == repeatCount - 2:
        max.append(word)
print("#9", "re.compile('\\b([aeiou]*[^ \\naeiou][aeiou]*){" + str(1) + ",}\\b')")
r = 2
while r < repeatCount - 1:
    print("re.compile('\\b([aeiou]*[^ \\naeiou][aeiou]*){" + str(r) + ",}\\b')")
    r += 1
print(len(max), "total matches")
for word in max[0:5]:
    print(word)
print('\n')

# Regular Expression 10
word  = ""
less = []
moreThanTwo = set()
max = []
maxLength = 0
regularExpression = re.compile(r"(\w)+(\w*\1\w*){2,}")

for result in regularExpression.finditer(stringLine):
    start, end = result.span()
    for char in range(start, end):
        word += stringLine[char]
    moreThanTwo.add(word)
    word = ""
for word in stringLine.split():
    if word not in moreThanTwo:
        less.append(word)
        if len(word) > maxLength:
            maxLength = len(word)
for word in less:
    if len(word) == maxLength:
        max.append(word)
print("#10", regularExpression)
print(len(max), "total matches")
for word in max[0:5]:
    print(word)
print('\n')
