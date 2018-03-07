from random import random
import numpy as np
from random import randint

class SimulatedAnnealing:
    ''''''
    def __init__(self, queens, n):
        self.queens = queens
        self.n = n
        #print(self.queens)
        while self.cost(self.queens, n) != 0:
            self.anneal(self.queens, n)

    def anneal(self, queens, n):
        currentCost = self.cost(self.queens, n)
        T = 1.0
        T_min = 0.00001
        alpha = 0.9
        while T > T_min:
            i = 1
            print("T : ", T)
            while i <= 100:
                next = self.randomNeighbour(self.queens, n)
                #print(next)
                nextCost = self.cost(next, n)
                #print(nextCost)
                #("current: ", currentCost)
                a = np.exp((nextCost - currentCost)/T)
                print("a : ", a)
                if a > random():
                    self.queens = next
                    currentCost = nextCost
                    #print(currentCost)
                '''else:
                    self.neighbourEval(self.queens, n)'''
                i += 1
            '''T = T*alpha'''
            T0 = T
            T = alpha / (np.log(T + T0))
            #print(queens)

    def neighbourEval(self, queens, n):

        queensTemp = queens[:]
        minCost = 2000
        #iterate through queens
        for i in range(n):
            #iterate through rows
            for j in range(n):
                #check if the queen is in the same position
                if j == queens[i]:
                    j = j + 1
                else:
                    #move queen to the next row
                    queensTemp[i] = j
                    #determine cost for current position
                    cost = self.cost(queensTemp, n)

                    if cost < minCost:
                        #store the best position and its cost so far
                        bestColumn = i
                        bestRow = j
                        minCost = cost

                        #print("Column: ", minCost)

                        if minCost == 0:
                            self.queens[bestColumn] = bestRow

            queensTemp = queens[:]
        self.queens[bestColumn] = bestRow
        #print("Board: ", minCost)
        #print(self.cost(queens, n))


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