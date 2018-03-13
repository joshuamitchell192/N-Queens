from random import random
import numpy as np
from random import randint
import time

class Genetic:
    def __init__(self, queens, n):

        self.queens = queens
        self.n = n
        self.printBoard(self.queens, n)
        start = time.time()

        end = time.time()
        print(end - start)


    def cost(self, queens, n):
        conflicts = 0

        for i in range(n):
            for j in range(i + 1, n):
                if i != j:
                    # Horizontal axis
                    if queens[i] == queens[j]:
                        conflicts = conflicts + 1
                    # Diagonal Axis Positive
                    if abs(queens[i] - queens[j]) == abs(i - j):
                        conflicts = conflicts + 1
        return int(conflicts)

    def printBoard(self, queens, n):

        for i in range(n):

            print("|", end='')
            for j in range(n):

                if queens[j] == i:
                    print(" x |", end='')

                else:
                    print("   |", end='')

            print("\n")