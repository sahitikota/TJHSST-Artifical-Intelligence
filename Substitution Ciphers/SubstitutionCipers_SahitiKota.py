# Sahiti Kota
# 02/24/2022 
from math import log
import random
import sys
with open('ngrams.txt') as f:
        frequencyDict = {line.split()[0] : int(line.split()[1]) for line in f}

# global constants
POPULATION_SIZE = 500
NUM_CLONES = 2
TOURNAMENT_SIZE = 30
TOURNAMENT_WIN_PROBABILITY = .75
CROSSOVER_LOCATIONS = 5
MUTATION_RATE = .8

def encodeCipher(message, cipher):
    message = message.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    punctuationIndexes = []
    ind = 0
    cipherList = list(cipher)
    alphabetList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    encoded = ""
    for char in message:
        if char not in alphabet:
            message = message.replace(char, '')
            punctuationIndexes.append((ind, char))
        ind += 1
    for char in message:
        index = alphabetList.index(char)
        encoded += cipherList[index]
    encodedPunct = list(encoded)
    for index, punct in punctuationIndexes:
        encodedPunct.insert(index, punct)
    encodedPunctString = ""
    for item in encodedPunct:
        encodedPunctString += item
    return encodedPunctString

def decodeCipher(message, cipher):
    message = message.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    punctuationIndexes = []
    ind = 0
    cipherList = list(cipher)
    alphabetList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    decoded = ""
    for char in message:
        if char not in alphabet:
            message = message.replace(char, '')
            punctuationIndexes.append((ind, char))
        ind += 1
    for char in message:
        index = cipherList.index(char)
        decoded += alphabetList[index]
    encodedPunct = list(decoded)
    for index, punct in punctuationIndexes:
        encodedPunct.insert(index, punct)
    encodedPunctString = ""
    for item in encodedPunct:
        encodedPunctString += item
    return encodedPunctString

def testFitness(n, encoded, cipher):
    decoded = decodeCipher(encoded, cipher)
    nGramsScore = 0
    chunks = [decoded[i: i + n] for i in range(0, len(decoded))]
    for chunk in chunks:
        if chunk in frequencyDict:
            nGramsScore += (log(frequencyDict[chunk], 2))
    return nGramsScore

def hillClimbing(encoded):
    x = 0
    alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    alphaList = alphabet.split(" ")
    random.shuffle(alphaList)
    cipher = ''.join(alphaList)
    baseFitness = testFitness(4, encoded, cipher)
    print(decodeCipher(encoded, cipher))
    while x <= 10:
        random.shuffle(alphaList)
        cipher = ''.join(alphaList)
        fitness = testFitness(4, encoded, cipher)
        if fitness > baseFitness:
            baseFitness = fitness
            print(fitness, decodeCipher(encoded, cipher))
            print('\n')

def generatePopulation():
    alphabet = "E T A O I N S H R D L C U M W F G Y P B V K X J Q Z"
    alphaList = alphabet.split(" ")
    population = []
    for i in range(POPULATION_SIZE):
        random.shuffle(alphaList)
        cipher = ''.join(alphaList)
        population.append(cipher)
    #print("g done")
    return population

def selection(generation, message, genFitness):
    tournamentMembers = random.sample(generation, 2 * TOURNAMENT_SIZE)
    tournamentOne = tournamentMembers[0:TOURNAMENT_SIZE]
    tournamentTwo = tournamentMembers[TOURNAMENT_SIZE: 2 * TOURNAMENT_SIZE]
    t1fitness = []
    t2fitness = []
    for strategy in tournamentOne:
        t1fitness.append((genFitness[strategy], strategy))
    t1fitness.sort(reverse = True)
    p1Chosen = False
    t1parent = ""
    while p1Chosen == False:
        if random.random() < TOURNAMENT_WIN_PROBABILITY:
            t1parent = t1fitness[0][1]
            p1Chosen = True
        else:
            t1fitness.pop(0)
    for strategy in tournamentTwo:
        t2fitness.append((genFitness[strategy], strategy))
    t2fitness.sort(reverse = True)
    p2Chosen = False
    t2parent = ""
    while p2Chosen == False:
        if random.random() < TOURNAMENT_WIN_PROBABILITY:
            t2parent = t2fitness[0][1]
            p2Chosen = True
        else:
            t2fitness.pop(0)
    #print("s done")
    return t1parent, t2parent

def breeding(parents):
    t1parent, t2parent = parents
    parentOne = random.choice(parents)
    if parentOne == t1parent:
        parentTwo = t2parent
    else:
        parentOne = t2parent
        parentTwo = t1parent
    indices = [i for i in range(26)]
    p1CrossIndices = random.sample(indices, CROSSOVER_LOCATIONS)
    child = ["" for i in range(26)]
    for index in p1CrossIndices:
            child[index] = parentOne[index]
    for letter in parentTwo:
        if letter not in child:
            child[child.index("")] = letter
    if random.random() < MUTATION_RATE:
        swap = random.sample(indices, 2)
        firstLetter = child[swap[0]]
        secondLetter = child[swap[1]]
        child[swap[0]] = secondLetter
        child[swap[1]] = firstLetter
    childCipher = ''.join(child)
    #print("b done")
    return childCipher
    
x = 0
message = sys.argv[1]
gen = generatePopulation()
genFitness = {}
for strategy in gen:
        fitness = testFitness(4, message, strategy)
        genFitness[strategy] = fitness
while x < 500:
    nextGen = []
    ranks = []
    ranks = sorted(genFitness.items(), key = lambda x: x[1], reverse = True)
    for i in range(NUM_CLONES):
        nextGen.append(ranks[i][0])
    while len(nextGen) < POPULATION_SIZE:
        child = breeding(selection(gen, message, genFitness))
        if child not in nextGen:
            nextGen.append(child)
    nextGenFitness = {}
    for strategy in nextGen:
        fitness = testFitness(4, message, strategy)
        nextGenFitness[strategy] = fitness
    gen = nextGen
    genFitness = nextGenFitness
    ranks = sorted(genFitness.items(), key = lambda x: x[1], reverse = True)
    bestStrategy = ranks[0][0]
    print(decodeCipher(message, bestStrategy))
    print('\n')
    x += 1
    