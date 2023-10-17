# Sahiti Kota
# 01/29/2022
from colorama import init, Back, Fore
import re
import sys

init()

regEx = sys.argv[1]
mod = regEx[1:]
flags = ""
if mod.index('/') != len(mod):
    flags = mod[mod.index('/') + 1:]
    mod = mod[:mod.index('/')]

if len(flags) == 0:
    regularExpression = re.compile(mod)
elif len(flags) == 1:
    if flags == 'i':
        regularExpression = re.compile(mod, re.I)
    elif flags == 'm':
        regularExpression = re.compile(mod, re.M)
    elif flags == 's':
        regularExpression = re.compile(mod, re.S)
elif len(flags) == 2:
    if flags == 'im' or flags == 'mi':
        regularExpression = re.compile(mod, re.I | re.M)
    elif flags == 'is' or flags == 'si':
        regularExpression = re.compile(mod, re.I | re.S)
    if flags == 'sm' or flags == 'ms':
        regularExpression = re.compile(mod, re.S | re.M)
elif len(flags) == 3:
    regularExpression = re.compile(mod, re.S | re.M | re.I)

s = "While inside they wined and dined, safe from the howling wind.\nAnd she whined, it seemed, for the 100th time, into the ear of her friend,\nWhy indeed should I wind the clocks up, if they all run down in the end?"

highlighted = ""
indices = []
startEnd = []
color = Back.LIGHTMAGENTA_EX
for result in regularExpression.finditer(s):
    start, end = result.span()
    startEnd.append((start, end))
    for char in range(start, end):
        indices.append(char)
    indices.append("x")

switch = False
for ind in range(len(s)):
    if ind not in indices:
        highlighted += s[ind]
    else:
        if switch == True:
            color = Back.LIGHTBLUE_EX
            highlighted += color + s[ind] + Back.RESET
            if indices[indices.index(ind) + 1] == "x":
                switch = False
                color = Back.LIGHTMAGENTA_EX
        elif indices[indices.index(ind) + 1] == "x" and indices.index(ind) + 1 != len(indices) - 1:
            highlighted += color + s[ind] + Back.RESET
            if indices[indices.index(ind) + 2] == ind + 1:
                switch = True
        else:
            highlighted += color + s[ind] + Back.RESET

print(highlighted)
        