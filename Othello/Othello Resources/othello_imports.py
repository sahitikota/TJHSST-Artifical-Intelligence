# Sahiti Kota
# 11/28/2021

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
    # this does not work 16 to 31, 4 to 15, 34 to 53
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
    # if chaning spaces to the diagonal top left
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