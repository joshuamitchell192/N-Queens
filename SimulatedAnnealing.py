from random import random
import numpy as np
from random import randint
import matplotlib.pyplot as plt
import time


class SimulatedAnnealing:
    """Find an optimal solution by decreasing the probability of selecting a random neighbour
       as the temperature T decreases"""
    def __init__(self, queens, n):

        self.queens = queens
        self.n = n
        # print initial board state
        self.printBoard(self.queens, n)
        # start timer
        start = time.time()
        self.anneal(n)
        end = time.time()

        # print board and runtime after solution is found
        self.printBoard(self.queens, n)
        print("Runtime:", end - start, "(seconds)")


    def anneal(self, n):
        currentCost = self.cost(self.queens, n)

        # Continue to search until a goal node is reached
        while self.cost(self.queens, n) != 0:

            T = 1.0
            T0 = 1.0
            T_min = 0.0001
            alpha = 0.9

            # Reduce the temperature until the threshold is reached
            while T > T_min:

                i = 1
                # print the goal node cost and its queen locations
                if currentCost == 0 and T <= T_min:
                    print('\r', "Cost:", currentCost, self.queens, end='\n', flush=True)
                else:
                    print('\r', "Cost:", currentCost, self.queens, "queens:", n, end='', flush=True)

                # Choose 100 random neighbours and apply the acceptance probability
                while i <= 100:

                    # Find random neighbour
                    nextState = self.randomNeighbour(self.queens, n)
                    # Evaluate Cost of random neighbour
                    nextCost = self.cost(nextState, n)
                    # Determine acceptance probabiltiy for given current state and random neighbour
                    a = np.exp(-(nextCost - currentCost)/T)

                    # Select random neighbour if acceptance probability is greater than random value
                    if a > random():
                        self.queens = nextState
                        currentCost = nextCost
                        if currentCost == 0:
                            break

                    i += 1

                if currentCost == 0:
                    break

                # Decrease temperature
                T = T*alpha

    def randomNeighbour(self, queens, n):

        queensTemp = queens[:]

        # Select a random row and column for the random neighbour
        i = randint(0, n-1)
        j = randint(0, n-1)

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
