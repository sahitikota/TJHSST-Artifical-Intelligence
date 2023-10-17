# Sahiti Kota
# 11/14/2021

import sys

# You are given code to read in a puzzle from the command line.  The puzzle should be a single input argument IN QUOTES.
# A puzzle looks like this: "56 56 28x14 32x11 32x10 21x18 21x18 21x14 21x14 17x14 28x7 28x6 10x7 14x4"
# The code below breaks it down:
puzzle = "56 56 28x14 32x11 32x10 21x18 21x18 21x14 21x14 17x14 28x7 28x6 10x7 14x4".split()
puzzle_height = int(puzzle[0])
puzzle_width = int(puzzle[1])
rectangles = [(int(temp.split("x")[0]), int(temp.split("x")[1])) for temp in puzzle[2:]]
# puzzle_height is the height (number of rows) of the puzzle
# puzzle_width is the width (number of columns) of the puzzle
# rectangles is a list of tuples of rectangle dimensions

# INSTRUCTIONS:
#
# First check to see if the sum of the areas of the little rectangles equals the big area.
# If not, output precisely this - "Containing rectangle incorrectly sized."
# correctly done
def checkSum(pHeight, pWidth, rectangles):
    bigArea = pWidth * pHeight
    overallArea = 0
    for rectangle in rectangles:
        height, width = rectangle
        overallArea += (height * width)
    if bigArea == overallArea:
        return True
    return "Containing rectangle incorrectly sized."
print(checkSum(puzzle_height, puzzle_width, rectangles))

# Then try to solve the puzzle.
# If the puzzle is unsolvable, output precisely this - "No solution."

def createBoard(pHeight, pWidth):
    return [[0 for x in range(pWidth)] for y in range(pHeight)] 

def rotatePiece(piece):
    height, width = piece
    return (width, height)

def completedParts(board):
    completedList = []
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 1:
                completedList.append((row, column))
    return completedList

def goalTest(board):
    for row in board:
        for column in board:
            if board[row][column] == 0:
                return False
    return True


# If the puzzle is solved, output ONE line for EACH rectangle in the following format:
# row column height width
# where "row" and "column" refer to the rectangle's top left corner.
#
# For example, a line that says:
# 3 4 2 1
# would be a rectangle whose top left corner is in row 3, column 4, with a height of 2 and a width of 1.
# Note that this is NOT the same as 3 4 1 2 would be.  The orientation of the rectangle is important.
#
# Your code should output exactly one line (one print statement) per rectangle and NOTHING ELSE.
# If you don't follow this convention exactly, my grader will fail.