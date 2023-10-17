# Sahiti Kota
# 10/11/2021

import random
# board size is always 6 x 6
carRepresentationList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "!"]
truckRepresentationList = ["@", "#", "$", "%"]
def generatePuzzle():
    # car always starts at the same position
    puzzleString = "............CC......................"
    # maximum 11 blocking cars, randomly placing a number of them
    overallNumBlockingCars = random.randint(0, 11)
    blockingCarCount = 0
    # while the number of cars to place hasn't been placed
    while blockingCarCount != overallNumBlockingCars:
        # choosing to be vertical or horizontal
        position = random.randint(0, 1)
        # placing car vertically
        if position == 0:
            firstBoxIndex = random.randint(0, 35)
            if firstBoxIndex + 6 < 35:
                if puzzleString[firstBoxIndex] == "." and puzzleString[firstBoxIndex + 6] == ".":
                    blockingCarCount += 1
                    puzzleString = puzzleString[:firstBoxIndex] + carRepresentationList[blockingCarCount - 1] + puzzleString[firstBoxIndex + 1:]
                    puzzleString = puzzleString[:firstBoxIndex + 6] + carRepresentationList[blockingCarCount - 1] + puzzleString[firstBoxIndex + 7:]
            # placing car horizontally
        elif position == 1:
            firstBoxIndex = random.randint(0, 35)
            # checking if second index for car is in range and on the same line
            if firstBoxIndex + 1 < 35 and (firstBoxIndex + 1) % 6 != 0:
                if puzzleString[firstBoxIndex] == "." and puzzleString[firstBoxIndex + 1] == ".":
                    blockingCarCount += 1
                    puzzleString = puzzleString[:firstBoxIndex] + carRepresentationList[blockingCarCount - 1] + puzzleString[firstBoxIndex + 1:]
                    puzzleString = puzzleString[:firstBoxIndex + 1] + carRepresentationList[blockingCarCount - 1] + puzzleString[firstBoxIndex + 2:]
    # maximum 4 blocking trucks, randomly placing a number of them
    overallNumBlockingTrucks = random.randint(0, 4)
    blockingTruckCount = 0
    # while the number of trucks to place hasn't been placed
    while blockingTruckCount != overallNumBlockingTrucks:
        # choosing to be vertical or horizontal
        position = random.randint(0, 1)
        # placing truck vertically
        if position == 0:
            firstBoxIndex = random.randint(0, 35)
            if firstBoxIndex + 6 < 35 and firstBoxIndex + 12 < 36:
                if puzzleString[firstBoxIndex] == "." and puzzleString[firstBoxIndex + 6] == "." and puzzleString[firstBoxIndex + 12] == ".":
                    blockingTruckCount += 1
                    puzzleString = puzzleString[:firstBoxIndex] + truckRepresentationList[blockingTruckCount - 1] + puzzleString[firstBoxIndex + 1:]
                    puzzleString = puzzleString[:firstBoxIndex + 6] + truckRepresentationList[blockingTruckCount - 1] + puzzleString[firstBoxIndex + 7:]
                    puzzleString = puzzleString[:firstBoxIndex + 12] + truckRepresentationList[blockingTruckCount - 1] + puzzleString[firstBoxIndex + 13:]
        # placing truck horizontally
        elif position == 1:
            firstBoxIndex = random.randint(0, 35)
            # checking if second and third index for truck is in range and on the same line
            if firstBoxIndex + 1 < 35 and (firstBoxIndex + 1) % 6 != 0 and firstBoxIndex + 2 < 35 and (firstBoxIndex + 2) % 6 != 0:
                if puzzleString[firstBoxIndex] == "." and puzzleString[firstBoxIndex + 1] == "." and puzzleString[firstBoxIndex + 2] == ".":
                    blockingTruckCount += 1
                    puzzleString = puzzleString[:firstBoxIndex] + truckRepresentationList[blockingTruckCount - 1] + puzzleString[firstBoxIndex + 1:]
                    puzzleString = puzzleString[:firstBoxIndex + 1] + truckRepresentationList[blockingTruckCount - 1] + puzzleString[firstBoxIndex + 2:]
                    puzzleString = puzzleString[:firstBoxIndex + 2] + truckRepresentationList[blockingTruckCount - 1] + puzzleString[firstBoxIndex + 3:]
    return puzzleString

def getChildren(puzzleString):
    childrenList = []
    puzzleList = list(puzzleString)
    for index in range(len(puzzleString)):
        # if car can move, move once forward horizontally
        if puzzleString[index] == "C" and puzzleString[index + 1] == "C":
            if index + 2 < 35:
                if puzzleString[index + 2] == ".":
                    puzzleList[index] = "."
                    puzzleList[index + 2] = "C"
                    newPuzzleString = "".join(puzzleList)
                    childrenList.append(newPuzzleString)
                    boardList = list(puzzleString)
        # if car can move, move once backward horizontally
            if index - 1 > 0:
                if puzzleString[index - 1] == ".":
                    puzzleList[index] = "."
                    puzzleList[index - 1] = "C"
                    newPuzzleString = "".join(puzzleList)
                    childrenList.append(newPuzzleString)
                    boardList = list(puzzleString)
        # if it is a blocking car
        elif puzzleString[index] in carRepresentationList:
            if puzzleString[index + 1] == puzzleString[index]:
            # if blocking car is horizontal and can move once forward
                if index + 2 < 35:
                    if puzzleString[index + 2] == ".":
                        puzzleList[index] = "."
                        puzzleList[index + 2] = puzzleString[index]
                        newPuzzleString = "".join(puzzleList)
                        childrenList.append(newPuzzleString)
                        boardList = list(puzzleString)
                # if blocking car can move, move once backward horizontally
                if index - 1 > 0 :
                    if puzzleString[index - 1] == ".":
                        puzzleList[index] = "."
                        puzzleList[index - 1] = puzzleString[index]
                        newPuzzleString = "".join(puzzleList)
                        childrenList.append(newPuzzleString)
                        boardList = list(puzzleString)
            elif puzzleString[index + 6] == puzzleString[index]:
                # if blocking car can move, move once forward vertically
                if index + 12 < 35:
                    if puzzleString[index + 12] == ".":
                        puzzleList[index] = "."
                        puzzleList[index + 12] = puzzleString[index]
                        newPuzzleString = "".join(puzzleList)
                        childrenList.append(newPuzzleString)
                        boardList = list(puzzleString)
                # if blocking car can move, move once backward vertically
                if index - 6 > 0:
                    if puzzleString[index - 6] == ".":
                        puzzleList[index] = "."
                        puzzleList[index - 6] = puzzleString[index]
                        newPuzzleString = "".join(puzzleList)
                        childrenList.append(newPuzzleString)
                        boardList = list(puzzleString)
        # if it is a blockign truck
        elif puzzleString[index] in truckRepresentationList:
            if puzzleString[index + 2] == puzzleString[index]:
                # move horizontally forward
                if index + 3 < 35:
                    if puzzleString[index + 3] == '.':
                        puzzleList[index] = "."
                        puzzleList[index + 3] = puzzleString[index]
                        newPuzzleString = "".join(puzzleList)
                        childrenList.append(newPuzzleString)
                        boardList = list(puzzleString)
                # move horizontally backward
                if index - 1 > 0 and index + 2 < 35:
                    if puzzleString[index - 1] == ".":
                        puzzleList[index + 2] = "."
                        puzzleList[index - 1] = puzzleString[index]
                        newPuzzleString = "".join(puzzleList)
                        childrenList.append(newPuzzleString)
                        boardList = list(puzzleString)
            if index + 12 < 35:
                if puzzleString[index + 12] == puzzleString[index]:
                    # move vertically forward (down)
                    if index + 18 < 35:
                        if puzzleString[index + 18] == '.':
                            puzzleList[index] = "."
                            puzzleList[index + 18] = puzzleString[index]
                            newPuzzleString = "".join(puzzleList)
                            childrenList.append(newPuzzleString)
                            boardList = list(puzzleString)
                    # move vertically forward (up)
                    if index - 6 > 0 and index + 12 < 35:
                        if puzzleString[index - 6] == '.':
                            puzzleList[index + 12] = "."
                            puzzleList[index - 6] = puzzleString[index]
                            newPuzzleString = "".join(puzzleList)
                            childrenList.append(newPuzzleString)
                            boardList = list(puzzleString)
    return childrenList


def goalTest(puzzleString):
    if puzzleString.find("CC") == 16:
        return True
    return False

def printPuzzle(puzzleString):
    toPrint = ""
    for index in range (0, len(puzzleString)):
        if index % 6 != 0:
            toPrint += puzzleString[index] + " "
        elif index % 6 == 0:
            toPrint += '\n'
            toPrint += puzzleString[index] + " "
    return toPrint

print(printPuzzle(generatePuzzle()))
for puzzle in getChildren(generatePuzzle()):
    print(printPuzzle(puzzle))