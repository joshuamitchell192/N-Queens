from random import random
import numpy as np
from random import randint
import time
import operator

class Genetic:
    def __init__(self, n):

        #self.queens = queens
        # TODO - create the starting population
        self.n = n
        #self.printBoard(self.queens, n)
        start = time.time()
        self.genetic(n)
        end = time.time()
        print(end - start)

    def genetic(self, n):
        population = self.population(n, 50)


    def crossover(self, x, y, n):
        # select a random point to merge both configurations
        crossOverPoint = randint(0, n-1)



    def population(self, n, populationSize):
        population = []

        # produce the initial population
        for p in range(populationSize):
            population.append([])
            population[p] = ([randint(0, n-1) for x in range(n)])
            population.sort(key=operator.methodcaller('self.fitness'))
        # Order the population in terms of their fitness values


        for p in range(populationSize):
            print(self.fitness(population[p], n))


#print(population)

        return population

    def fitness(self, queens, n):
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