# Sahiti Kota
# 03/06/2022
import sys

# gameboard - height 20, width 10 (row major order)
boardString = sys.argv[1]

# translating board string to a list of lists, [19][9] - row, column
def translateBoard(boardString):
    board = []
    lowerBound = 0
    upperBound = 10
    while upperBound <= 200:
        board.append(list(boardString[lowerBound:upperBound]))
        lowerBound += 10
        upperBound += 10
    return board

board = translateBoard(boardString)

def printBoard(board):
    for row in board:
        rowString  = ''
        for index in row:
            rowString += index
        print(rowString)

def clearRows(board):
    while ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'] in board:
        board.remove(['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'])
        board.insert(0, [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def findColumnHeights(board):
    columns =  [[], [], [], [], [], [], [], [], [], []]
    for row in board:
        for column in range(len(board)):
            if column == 0:
                columns[0].append(row[column])
            elif column == 1:
                columns[1].append(row[column])
            elif column == 2:
                columns[2].append(row[column])
            elif column == 3:
                columns[3].append(row[column])
            elif column == 4:
                columns[4].append(row[column])
            elif column == 5:
                columns[5].append(row[column])
            elif column == 6:
                columns[6].append(row[column])
            elif column == 7:
                columns[7].append(row[column])
            elif column == 8:
                columns[8].append(row[column])
            elif column == 9:
                columns[9].append(row[column])
    heights = []
    for column in columns:
        filled = []
        for row in range(len(column)):
            if column[row] == "#":
                # need to be able to find the highest place with a # (overhang)
                filled.append(20 - row)
        if len(filled) > 0:
            heights.append(max(filled))
        else:
            heights.append(0)
    return heights

pieceSpaces = {'i0': [0, 0, 0, 0], 'i1': [0], 'o0': [0, 0], 't0': [0, 0, 0], 't1': [0, 1], 't2': [1, 0, 1], 't3': [1, 0], 's0': [0, 0, 1], 's1': [1, 0], 'z0': [1, 0, 0], 'z1': [0, 1], 'j0': [0, 0, 0], 'j1': [0, 2], 'j2': [1, 1, 0], 'j3': [0, 0], 'l0': [0, 0, 0], 'l1': [0, 0], 'l2': [0, 1, 1], 'l3': [2, 0]}
pieceList = list(pieceSpaces.keys())
dashHeights = {'i0': [1, 1, 1, 1], 'i1': [4], 'o0': [2, 2], 't0': [1, 2, 1], 't1': [3, 1], 't2': [1, 2, 1], 't3': [1, 3], 's0': [1, 2, 1], 's1': [2, 2], 'z0': [1, 2, 1], 'z1': [2, 2], 'j0': [2, 1, 1], 'j1': [3, 1], 'j2': [1, 1, 2], 'j3': [1, 3], 'l0': [1, 1, 2], 'l1': [3, 1], 'l2': [2, 1, 1], 'l3': [1, 3]}

def findLocations(piece, board, heights):
    places = []
    spaces = pieceSpaces[piece]
    span = len(spaces)
    leftMost = 0
    while leftMost + span - 1 < 10:
        boardHeights = heights[leftMost: leftMost + span]
        subtracted = []
        for index in range(len(boardHeights)):
            subtracted.append(boardHeights[index] - spaces[index])
        row = max(subtracted)
        places.append((leftMost, row))
        leftMost += 1
    return places

def placePiece(piece, board, location):
    nB = toString(board)
    newBoard =  translateBoard(nB)
    column, row = location
    heights = dashHeights[piece]
    spaces = pieceSpaces[piece]
    for horizontal in range(len(heights)):
        rowIncrease = horizontal
        vertical = heights[horizontal]
        for x in range(vertical):
            if 19 - (row + x) - spaces[horizontal] < 0 or column + horizontal > 9:
                return "GAME OVER"
            else:
                newBoard[19 - (row + x) - spaces[horizontal]][column + horizontal] = '#'
    return newBoard

def toString(board):
    boardString = ""
    for row in board:
        for index in row:
            boardString += index
    return boardString

with open('tetrisout.txt', 'w') as f:
    for piece in pieceList:
        locations = findLocations(piece, board, findColumnHeights(board))
        for location in locations:
            newBoard = placePiece(piece, board, location)
            if newBoard != "GAME OVER":
                newBoard = clearRows(newBoard)
                newBoardString = toString(newBoard)
            f.write(toString(newBoard))
            f.write('\n')
            # print(piece, location)
            # printBoard(newBoard)
            newBoard = board