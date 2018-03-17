from random import random
import numpy as np
from random import randint
import time


class SimulatedAnnealing:
    ''''''
    def __init__(self, queens, n):
        self.queens = queens
        self.n = n
        self.printBoard(self.queens, n)
        start = time.time()
        self.anneal(self.queens, n)
        end = time.time()

        self.printBoard(self.queens, n)
        print("Runtime:", end - start, "(seconds)")
    def anneal(self, queens, n):

        currentCost = self.cost(self.queens, n)
        while self.cost(self.queens, n) != 0:
            T = 1.0
            T0 = 1.0
            T_min = 0.0001
            alpha = 0.9

            while T > T_min:
                i = 1
                if currentCost == 0 and T <= T_min:
                    print('\r', "Cost:", currentCost, self.queens, end='\n', flush=True)
                else:
                    print('\r', "Cost:", currentCost, self.queens, end='', flush=True)


                while i <= 100:

                    next = self.randomNeighbour(self.queens, n)

                    nextCost = self.cost(next, n)

                    a = np.exp((currentCost - nextCost)/T)

                    if a > random():
                        self.queens = next
                        currentCost = nextCost

                    i += 1

                T = T*alpha
                '''T0 = T
                T = alpha / (np.log(T + T0))'''


    def randomNeighbour(self, queens, n):
        queensTemp = queens[:]

        i = randint(0, n-1)
        #print("i : ", i)
        j = randint(0, n-1)
        #print("j : ", j)

        queensTemp[i] = j

        return queensTemp[:]

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

        print("\n")
        for i in range(n):

            print("|", end='')
            for j in range(n):

                if queens[j] == i:
                    print(" x |", end='')

                else:
                    print("   |", end='')

            print("\n")