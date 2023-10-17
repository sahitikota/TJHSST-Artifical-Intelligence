# Sahiti Kota
# 12/02/2021
import sys
import math

def possible_moves(board, token):
    possibleMovesSpaces = []
    if token == "x":
        oppositeToken = "o"
    else:
        oppositeToken = "x"
    boardFrame = "???????????" + board[0:8] + "??" + board[8:16] + "??" + board[16:24] + "??" + board[24:32] + "??" + board[32:40] + "??" + board[40:48] + "??" + board[48:56] + "??" + board[56:64] + "???????????"
    for space in range(len(boardFrame)):
        if boardFrame[space] == token:
            # space below
            if boardFrame[space + 10] == oppositeToken:
                s = space + 20
                while boardFrame[s] != "?" and boardFrame[s] != token:
                    if boardFrame[s] == ".":
                        possibleMovesSpaces.append(s)
                        break
                    elif boardFrame[s] == oppositeToken:
                        s = s + 10
            # space above
            if boardFrame[space - 10] == oppositeToken:
                s = space - 20
                while boardFrame[s] != "?" and boardFrame[s] != token:
                    if boardFrame[s] == ".":
                        possibleMovesSpaces.append(s)
                        break
                    elif boardFrame[s] == oppositeToken:
                        s = s - 10
            # space horizontal right
            # this method works!!! need to implement for all directions
            if boardFrame[space + 1] == oppositeToken:
                s = space + 2
                while boardFrame[s] != "?" and boardFrame[s] != token:
                    if boardFrame[s] == ".":
                        possibleMovesSpaces.append(s)
                        break
                    elif boardFrame[s] == oppositeToken:
                        s = s + 1
            # space horizontal left
            if boardFrame[space - 1] == oppositeToken:
                s = space - 2
                while boardFrame[s] != "?" and boardFrame[s] != token:
                    if boardFrame[s] == ".":
                        possibleMovesSpaces.append(s)
                        break
                    elif boardFrame[s] == oppositeToken:
                        s = s - 1
            # space diagonal bottom right
            if boardFrame[space + 11] == oppositeToken:
                s = space + 22
                while boardFrame[s] != "?" and boardFrame[s] != token:
                    if boardFrame[s] == ".":
                        possibleMovesSpaces.append(s)
                        break
                    elif boardFrame[s] == oppositeToken:
                        s = s + 11
            # space diagonal bottom left
            if boardFrame[space + 9] == oppositeToken:
                s = space + 18
                while boardFrame[s] != "?" and boardFrame[s] != token:
                    if boardFrame[s] == ".":
                        possibleMovesSpaces.append(s)
                        break
                    elif boardFrame[s] == oppositeToken:
                        s = s + 9
            # space diagonal top right
            if boardFrame[space - 9] == oppositeToken:
                s = space - 18
                while boardFrame[s] != "?" and boardFrame[s] != token:
                    if boardFrame[s] == ".":
                        possibleMovesSpaces.append(s)
                        break
                    elif boardFrame[s] == oppositeToken:
                        s = s - 9
            # space diagonal top left
            if boardFrame[space - 11] == oppositeToken:
                s = space - 22
                while boardFrame[s] != "?" and boardFrame[s] != token:
                    if boardFrame[s] == ".":
                        possibleMovesSpaces.append(s)
                        break
                    elif boardFrame[s] == oppositeToken:
                        s = s - 11
    adjustedPossibleMoves = []
    adj = []
    for item in possibleMovesSpaces:
        adj.append(item - ((math.floor(item/ 10) - 2) * 2) - 13)
    [adjustedPossibleMoves.append(x) for x in adj if x not in adjustedPossibleMoves]
    return adjustedPossibleMoves

def make_move(board, token, index):
    board = board[:index] + token + board[index + 1:]
    if token == "x":
        oppositeToken = "o"
    else:
        oppositeToken = "x"
    boardFrame = "???????????" + board[0:8] + "??" + board[8:16] + "??" + board[16:24] + "??" + board[24:32] + "??" + board[32:40] + "??" + board[40:48] + "??" + board[48:56] + "??" + board[56:64] + "???????????"
    # index = index + (round(index/ 10) * 2) + 11
    if index <= 7:
        index = index + 11
    elif index <= 15:
        index += 13
    elif index <= 23:
        index += 15
    elif index <= 31:
        index += 17
    elif index <= 39:
        index += 19
    elif index <= 47:
        index += 21
    elif index <= 55:
        index += 23
    elif index <= 63:
        index += 25
    # if changing tiles above
    if boardFrame[index - 10] == oppositeToken:
        ogBoardFrame = boardFrame
        i = index - 10
        while boardFrame[i] != token:
            if boardFrame[i] == "?" or boardFrame[i] == ".":
                boardFrame = ogBoardFrame
                break
            else:
                boardFrame = boardFrame[:i] + token + boardFrame[i + 1:]
                i = i - 10
    # if changing tiles below
    if boardFrame[index + 10] == oppositeToken:
        i = index + 10
        ogBoardFrame = boardFrame
        while boardFrame[i] != token:
            if boardFrame[i] == "?" or boardFrame[i] == ".":
                boardFrame = ogBoardFrame
                break
            else:
                boardFrame = boardFrame[:i] + token + boardFrame[i + 1:]
                i = i + 10
    # if changing tiles to the left
    if boardFrame[index - 1] == oppositeToken:
        i = index - 1
        ogBoardFrame = boardFrame
        while boardFrame[i] != token:
            if boardFrame[i] == "?" or boardFrame[i] == ".":
                boardFrame = ogBoardFrame
                break
            else:
                boardFrame = boardFrame[:i] + token + boardFrame[i + 1:]
                i = i - 1
    # if changing tiles to the right
    if boardFrame[index + 1] == oppositeToken:
        i = index + 1
        ogBoardFrame = boardFrame
        while boardFrame[i] != token:
            if boardFrame[i] == "?" or boardFrame[i] == ".":
                boardFrame = ogBoardFrame
                break
            else:
                boardFrame = boardFrame[:i] + token + boardFrame[i + 1:]
                i = i + 1
    # if changing tiles to the diagonal bottom right
    if boardFrame[index + 11] == oppositeToken:
        i = index + 11
        ogBoardFrame = boardFrame
        while boardFrame[i] != token:
            if boardFrame[i] == "?" or boardFrame[i] == ".":
                boardFrame = ogBoardFrame
                break
            else:
                boardFrame = boardFrame[:i] + token + boardFrame[i + 1:]
                i = i + 11
    # if changing spaces to the diagonal bottom left
    if boardFrame[index + 9] == oppositeToken:
        i = index + 9
        ogBoardFrame = boardFrame
        while boardFrame[i] != token:
            if boardFrame[i] == "?" or boardFrame[i] == ".":
                boardFrame = ogBoardFrame
                break
            else:
                boardFrame = boardFrame[:i] + token + boardFrame[i + 1:]
                i = i + 9
    # if changing spaces to the diagonal top right
    if boardFrame[index - 9] == oppositeToken:
        i = index - 9
        ogBoardFrame = boardFrame
        while boardFrame[i] != token:
            if boardFrame[i] == "?" or boardFrame[i] == ".":
                boardFrame = ogBoardFrame
                break
            else:
                boardFrame = boardFrame[:i] + token + boardFrame[i + 1:]
                i = i - 9
    # if changing spaces to the diagonal top left
    if boardFrame[index - 11] == oppositeToken:
        i = index - 11
        ogBoardFrame = boardFrame
        while boardFrame[i] != token:
            if boardFrame[i] == "?" or boardFrame[i] == ".":
                boardFrame = ogBoardFrame
                break
            else:
                boardFrame = boardFrame[:i] + token + boardFrame[i + 1:]
                i = i - 11
    board = boardFrame[11: 19] + boardFrame[21: 29] + boardFrame[31: 39] + boardFrame[41: 49] + boardFrame[51: 59] + boardFrame[61: 69] + boardFrame[71: 79] + boardFrame[81: 89]
    return board
def find_next_move(board, player, depth):
    if player == "x":
        return maxMove(board, depth)
    else:
        return minMove(board, depth)
   # Based on whether player is x or o, start an appropriate version of minimax
   # that is depth-limited to "depth".  Return the best available move.

# All your other functions
def gameIsOver(board):
    if board.count(".") == 0:
        return True
    return False

def score(board):
    score = 0
    cornersDict = {0: {1, 8, 9}, 7: {6, 14, 15}, 56: {57, 48, 49}, 63: {62, 54, 55}}
    for corner, adjacents in cornersDict.items():
        if board[corner] == "x":
            score = score + 10000
            for adjacent in adjacents:
                if board[adjacent] == "x":
                    score = score + 10
        elif board[corner] == "o":
            score = score - 10000
            for adjacent in adjacents:
                if board[adjacent] == "o":
                    score = score - 10
        else:
            for adjacent in adjacents:
                if board[adjacent] == "x":
                    score = score - 10
                elif board[adjacent] == "o":
                    score = score + 10
    borders = [board[2], board[3], board[4], board[5], board[16], board[24], board[32], board[40], board[58], board[59], board[60], board[61], board[23], board[31], board[39], board[47]]
    for border in borders:
        if border == "x":
            score = score + 20
        elif border == "o":
            score = score - 20
    score = score + len(possible_moves(board, "x")) + board.count("x")
    score = score - len(possible_moves(board, "o")) - board.count("o")
    return score


def maxStep(board, depth):
    boardCopy = board
    if gameIsOver(board) or depth == 0 or len(possible_moves(board, "x")) == 0:
        return score(board)
    results = []
    for index in possible_moves(board, "x"):
        nextBoard = make_move(boardCopy, "x", index)
        results.append(minStep(nextBoard, depth - 1))
    return max(results)

def minStep(board, depth):
    boardCopy = board
    if gameIsOver(board) or depth == 0 or len(possible_moves(board, "o")) == 0:
        return score(board)
    results = []
    for index in possible_moves(board, "o"):
        nextBoard = make_move(boardCopy, "o", index)
        results.append(maxStep(nextBoard, depth - 1))
    return min(results)

def maxMove(board, depth):
    results = []
    boardCopy = board
    for index in possible_moves(board, "x"):
        nextBoard = make_move(boardCopy, "x", index)
        results.append((minStep(nextBoard, depth - 1), index))
    maximum, ind = max(results)
    for step, index in results:
        if step == maximum:
            return index

def minMove(board, depth):
    results = []
    boardCopy = board
    for index in possible_moves(board, "o"):
        nextBoard = make_move(boardCopy, "o", index)
        results.append((maxStep(nextBoard, depth - 1), index))
    minimum, ind = min(results)
    for step, index in results:
        if step == minimum:
            return index
            
board = sys.argv[1]
player = sys.argv[2]
depth = 1
for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all
   print(find_next_move(board, player, depth))
   depth += 1