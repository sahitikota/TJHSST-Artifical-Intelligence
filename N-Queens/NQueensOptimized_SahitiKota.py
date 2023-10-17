# Sahiti Kota
# 12/31/2021

import random
import time

def testSolution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    return True

def solve(state):
    solution = []
    # correct
    if (len(state) % 6) != 2 and (len(state) % 6) != 3:
        for num in range(1, len(state) + 1):
            if num % 2 == 0:
                solution.append(num)
        for num in range(0, len(state) + 1):
            if num % 2 == 1:
                solution.append(num)
    else:
        even = []
        odd = []
        for num in range(1, len(state) + 1):
            if num % 2 == 0:
                even.append(num)
            if num % 2 == 1:
                odd.append(num)
        if (len(state) % 6) == 2:
            odd.remove(3)
            odd.remove(1)
            odd.remove(5)
            odd.insert(0, 3)
            odd.insert(1, 1)
            odd.append(5)
            solution = even + odd
        elif (len(state) % 6) == 3:
            odd.remove(3)
            odd.remove(1)
            odd.append(1)
            odd.append(3)
            even.remove(2)
            even.append(2)
            solution = even + odd
    return solution

start = time.perf_counter()
N = 8
solutions = []
while (time.perf_counter() - start) < 30 and N < 201:
    state = [None] * N
    solutions.append(solve(state))
    N += 1

for solution in solutions:
    print(testSolution(solution))