# Sahiti Kota
# 11/15/2021

import sys

def gameIsOver(board):
    row1 = board[0:3]
    row2 = board[3:6]
    row3 = board[6:9]
    column1 = board[0:7:3]
    column2 = board[1:8:3]
    column3 = board[2:9:3]
    forwardDiagonal = board[2:7:2]
    backwardDiagonal = board[0:9:4]
    possibleWinsList = [row1, row2, row3, column1, column2,
                        column3, forwardDiagonal, backwardDiagonal]
    arrangementWinList = []
    for arrangement in possibleWinsList:
        if '.' in arrangement:
            arrangementWinList.append(False)
        elif arrangement == "XXX" or arrangement == "OOO":
            arrangementWinList.append(True)
        else:
            arrangementWinList.append(False)
    if True in arrangementWinList:
        return True
    if '.' not in board:
        return True
    return False

def printBoard(board):
    row1 = board[0:3]
    row2 = board[3:6]
    row3 = board[6:9]
    print(row1, "   012")
    print(row2, "   345")
    print(row3, "   678")

def possibleNextBoards(board, currentPlayer):
    possiblePlacements = []
    possibleNextBoards = []
    for index in range(len(board)):
        if board[index] == ".":
            possiblePlacements.append(index)
    for index in possiblePlacements:
        possibleNextBoards.append(
            (board[:index] + currentPlayer + board[index + 1:], index))
    return possibleNextBoards

def minStep(board):
    if gameIsOver(board):
        return boardScore(board)
    results = []
    for nextBoard, index in possibleNextBoards(board, "O"):
        results.append(maxStep(nextBoard))
    return min(results)

def maxStep(board):
    if gameIsOver(board):
        return boardScore(board)
    results = []
    for nextBoard, index in possibleNextBoards(board, "X"):
        results.append(minStep(nextBoard))
    return max(results)

def currentPlayer(board):
    xCount = 0
    oCount = 0
    for i in board:
        if i == "X":
            xCount += 1
        if i == "O":
            oCount += 1

    if xCount == oCount:
        return "X"
    return "O"

def boardScore(board):
    row1 = board[0:3]
    row2 = board[3:6]
    row3 = board[6:9]
    column1 = board[0:7:3]
    column2 = board[1:8:3]
    column3 = board[2:9:3]
    forwardDiagonal = board[2:7:2]
    backwardDiagonal = board[0:9:4]
    possibleWinsList = [row1, row2, row3, column1, column2,
                        column3, forwardDiagonal, backwardDiagonal]
    arrangementWinList = []
    for arrangement in possibleWinsList:
        if '.' in arrangement:
            arrangementWinList.append((arrangement, False))
        elif arrangement == "XXX" or arrangement == "OOO":
            arrangementWinList.append((arrangement, True))
        else:
            arrangementWinList.append((arrangement, False))
    for arrangement, outcome in arrangementWinList:
        if outcome == True:
            if arrangement == "XXX":
                return 1
            if arrangement == "OOO":
                return -1
    return 0

def maxMove(board):
    results = []
    for nextBoard, index in possibleNextBoards(board, currentPlayer(board)):
        results.append((minStep(nextBoard), index))
    maximum, ind = max(results)
    for step, index in results:
        if step == maximum:
            return index

def minMove(board):
    results = []
    for nextBoard, index in possibleNextBoards(board, currentPlayer(board)):
        results.append((maxStep(nextBoard), index))
    minimum, ind = min(results)
    for step, index in results:
        if step == minimum:
            return index

def place(board, index, player):
    board = board[:index] + player + board[index + 1:]
    return board

def emptySpaces(board):
    empty = []
    for char in range(len(board)):
        if board[char] == '.':
            empty.append(char)
    emptyString = ', '.join([str(elem) for elem in empty])
    return emptyString

def printScoreX(board):
    result = boardScore(board)
    if result == 1:
        print('I win!')
    elif result == -1:
        print('You win!')
    else:
        print("We tied!")

def printScoreO(board):
    result = boardScore(board)
    if result == 1:
        print('You win!')
    elif result == -1:
        print('I win!')
    else:
        print("We tied!")

board = sys.argv[1]
if board == '.........':
    player = input("Should I be X or O? ")
    print()
else:
    player = currentPlayer(board)
if board == ".........":
    if player == "X":
        while(gameIsOver(board) == False):
            print("Current Board: ")
            printBoard(board)
            print()
            for string, index in possibleNextBoards(board, 'X'):
                result = minStep(string)
                resultString = ""
                if result == 0:
                    resultString = "a tie"
                elif result == 1:
                    resultString = "a win"
                else:
                    resultString = "a loss"
                print("Moving at", index, "results in", resultString)
            print()
            print("I choose space", maxMove(board))
            board = place(board, maxMove(board), 'X')
            print()
            print("Current Board: ")
            printBoard(board)
            print()
            if gameIsOver(board):
                printScoreX(board)
            else:
                print("You can move to any of these spaces:", emptySpaces(board))
                placement = int(input("Your choice? "))
                board = place(board, placement, 'O')
                print()
                if (gameIsOver(board)):
                    print("Current Board: ")
                    printBoard(board)
                    print()
                    printScoreX(board)
    if player == "O":
        while(gameIsOver(board) == False):
            print("Current Board: ")
            printBoard(board)
            print()
            print("You can move to any of these spaces:", emptySpaces(board))
            placement = int(input("Your choice? "))
            print()
            board = place(board, placement, 'X')
            print("Current Board: ")
            printBoard(board)
            print()
            if gameIsOver(board):
                printScoreO(board)
            else:
                for string, index in possibleNextBoards(board, 'O'):
                    result = maxStep(string)
                    resultString = ""
                    if result == 0:
                        resultString = "a tie"
                    elif result == -1:
                        resultString = "a win"
                    else:
                        resultString = "a loss"
                    print("Moving at", index, "results in", resultString)
                print()
                print("I choose space", minMove(board))
                board = place(board, minMove(board), 'O')
                print()
                if (gameIsOver(board)):
                    print("Current Board: ")
                    printBoard(board)
                    print()
                    printScoreO(board)
else:
    if player == "X":
        while(gameIsOver(board) == False):
            print("Current Board: ")
            printBoard(board)
            print()
            for string, index in possibleNextBoards(board, 'X'):
                result = minStep(string)
                resultString = ""
                if result == 0:
                    resultString = "a tie"
                elif result == 1:
                    resultString = "a win"
                else:
                    resultString = "a loss"
                print("Moving at", index, "results in", resultString)
            print()
            print("I choose space", maxMove(board))
            board = place(board, maxMove(board), 'X')
            print()
            print("Current Board: ")
            printBoard(board)
            print()
            if gameIsOver(board):
                printScoreX(board)
            else:
                print("You can move to any of these spaces:", emptySpaces(board))
                placement = int(input("Your choice? "))
                board = place(board, placement, 'O')
                print()
                if (gameIsOver(board)):
                    print("Current Board: ")
                    printBoard(board)
                    print()
                    printScoreX(board)
    if player == "O":
        while(gameIsOver(board) == False):
            print("Current Board: ")
            printBoard(board)
            print()
            for string, index in possibleNextBoards(board, 'O'):
                result = maxStep(string)
                resultString = ""
                if result == 0:
                    resultString = "a tie"
                elif result == 1:
                    resultString = "a loss"
                else:
                    resultString = "a win"
                print("Moving at", index, "results in", resultString)
            print()
            print("I choose space", minMove(board))
            board = place(board, minMove(board), 'O')   
            print()
            print("Current Board: ")
            printBoard(board)
            print()
            if gameIsOver(board):
                printScoreO(board)
            else:
                print("You can move to any of these spaces:", emptySpaces(board))
                placement = int(input("Your choice? "))
                board = place(board, placement, 'X')
                print()
                if (gameIsOver(board)):
                    print("Current Board: ")
                    printBoard(board)
                    print()
                    printScoreO(board)