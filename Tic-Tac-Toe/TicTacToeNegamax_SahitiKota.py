# Sahiti Kota
# 11/21/2021

import sys 

def boardScore(board, player):
    row1 = board[0:3]
    row2 = board[3:6]
    row3 = board[6:9]
    column1 = board[0:7:3]
    column2 = board[1:8:3]
    column3 = board[2:9:3]
    forwardDiagonal = board[2:7:2]
    backwardDiagonal = board[0:9:4]
    possibleWinsList = [row1, row2, row3, column1, column2, column3, forwardDiagonal, backwardDiagonal]
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
            if arrangement == "XXX" and player == "X":
                return 1
            elif arrangement == "XXX" and player == "O":
                return -1
            elif arrangement == "OOO" and player == "O":
                return 1
            elif arrangement == "OOO" and player == "X":
                return -1
    return 0

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
    elif '.' not in board:
        return True
    return False

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

# negamax function
def negamax(board, currentPlayer):
    # first checks if the game is over then returns score if it is
    if gameIsOver(board):
        return boardScore(board, currentPlayer)
    results = []
    # finds what the opposing player is
    if currentPlayer == "X":
        nextPlayer = "O"
    else:
        nextPlayer = "X"
    # goes through all the possible boards for the current player
    for nextBoard, index in possibleNextBoards(board, currentPlayer):
        # recursively calls the boards and next player, and negates it to see the result in the perspective of the current player
        results.append(-1 * negamax(nextBoard, nextPlayer))
    return max(results)

def negamaxMove(board, currentPlayer):
    results = []
    if currentPlayer == "X":
        nextPlayer = "O"
    else:
        nextPlayer = "X"
    for nextBoard, index in possibleNextBoards(board, currentPlayer):
        results.append(((-1 * (negamax(nextBoard, nextPlayer))), index))
    maximum, ind = max(results)
    for step, index in results:
        if step == maximum:
            return index

def printBoard(board):
    row1 = board[0:3]
    row2 = board[3:6]
    row3 = board[6:9]
    print(row1, "   012")
    print(row2, "   345")
    print(row3, "   678")

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

# printing win when loss and loss when win
board = '.........'
if board == '.........':
    player = input("Should I be X or O? ")
    print()
else:
    player = currentPlayer(board)
if player == "X":
    oppositePlayer = "O"
else:
    oppositePlayer = "X"
if board == ".........":
    if player == "X":
        while gameIsOver(board) == False:
            print("Current Board: ")
            printBoard(board)
            print()
            for string, index in possibleNextBoards(board, player):
                result = negamax(string, oppositePlayer)
                resultString = ""
                if result == 0:
                    resultString = "a tie"
                elif result == -1:
                    resultString = "a win"
                else:
                    resultString = "a loss"
                print("Moving at", index, "results in", resultString)
            print()
            print("I choose space", negamaxMove(board, player))
            print()
            board = place(board, negamaxMove(board, player), player)
            print("Current Board: ")
            printBoard(board)
            print()
            if gameIsOver(board):
                score  = boardScore(board, player)
                if score == 1:
                    print('I win!')
                elif score == 0:
                    print("We tied!")
                else:
                    print("You won!")
            else:
                print("You can move to any of these spaces:", emptySpaces(board))
                placement = int(input("Your choice? "))
                board = place(board, placement, oppositePlayer)
                print()
                if (gameIsOver(board)):
                    print("Current Board: ")
                    printBoard(board)
                    print()
                    score  = boardScore(board, player)
                    if score == 1:
                        print('I win!')
                    elif score == 0:
                        print("We tied!")
                    else:
                        print("You won!")
    if player == "O":
        while(gameIsOver(board) == False):
            print("Current Board: ")
            printBoard(board)
            print()
            print("You can move to any of these spaces:", emptySpaces(board))
            placement = int(input("Your choice? "))
            print()
            board = place(board, placement, oppositePlayer)
            print("Current Board: ")
            printBoard(board)
            print()
            if (gameIsOver(board)):
                print("Current Board: ")
                printBoard(board)
                print()
                score = boardScore(board, player)
                if score == 1:
                    print('I win!')
                elif score == 0:
                    print("We tied!")
                else:
                    print("You won!")
            else:
                for string, index in possibleNextBoards(board, player):
                    result = negamax(string, oppositePlayer)
                    resultString = ""
                    if result == 0:
                        resultString = "a tie"
                    elif result == -1:
                        resultString = "a win"
                    else:
                        resultString = "a loss"
                    print("Moving at", index, "results in", resultString)
                print()
                print("I choose space", negamaxMove(board, player))
                print()
                board = place(board, negamaxMove(board, player), player)
                if gameIsOver(board):
                    score  = boardScore(board, player)
                    if score == 1:
                        print('I win!')
                    elif score == 0:
                        print("We tied!")
                    else:
                        print("You won!")
else:
    while gameIsOver(board) == False:
            print("Current Board: ")
            printBoard(board)
            print()
            for string, index in possibleNextBoards(board, player):
                result = negamax(string, oppositePlayer)
                resultString = ""
                if result == 0:
                    resultString = "a tie"
                elif result == -1:
                    resultString = "a win"
                else:
                    resultString = "a loss"
                print("Moving at", index, "results in", resultString)
            print()
            print("I choose space", negamaxMove(board, player))
            print()
            board = place(board, negamaxMove(board, player), player)
            print("Current Board: ")
            printBoard(board)
            print()
            if gameIsOver(board):
                score  = boardScore(board, player)
                if score == 1:
                    print('I win!')
                elif score == 0:
                    print("We tied!")
                else:
                    print("You won!")
            else:
                print("You can move to any of these spaces:", emptySpaces(board))
                placement = int(input("Your choice? "))
                board = place(board, placement, oppositePlayer)
                print()
                if (gameIsOver(board)):
                    print("Current Board: ")
                    printBoard(board)
                    print()
                    score  = boardScore(board, player)
                    if score == 1:
                        print('I win!')
                    elif score == 0:
                        print("We tied!")
                    else:
                        print("You won!")

