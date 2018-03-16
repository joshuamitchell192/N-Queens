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
        cutoff = 20
        populationSize = 50

        population = self.population(n, populationSize)

        self.sortPopulation(population, n, 0, len(population) - 1)

        self.parentSelection(population, cutoff)

    def crossover(self, x, y):
        child = []
        # select a random point to merge both configurations
        crossOverPoint = randint(0, self.n-1)

        for i in range(crossOverPoint):
            child.append(x[i])
        for i in range(crossOverPoint, self.n + 1):
            child.append(y[i])
        print(child)
    def parentSelection(self, population, cutoff):
        for i in range(cutoff, len(population)):
            del population[i]
            print(population)

        for i in range(len(population)):
            x = population[i]
            y = randint(0, self.n-1)
            self.crossover(x, y)

    def population(self, n, populationSize):
        populationSize += 1
        population = []

        # produce the initial population
        for p in range(populationSize):
            population.append([])
            population[p] = ([randint(0, n-1) for x in range(n)])

        '''for p in range(populationSize):
            print(self.fitness(population[p], n))'''

        return population

    def sortPopulation(self, population, n, low, high):

        if low < high:
            partition = self.quickSort(population, low, high)

            self.sortPopulation(population, n, low, partition - 1)
            self.sortPopulation(population, n, partition + 1, high)

    def quickSort(self, population, low, high):


        i = low - 1
        pivot = self.fitness(population[high], self.n)
        for j in range(low, high):

            if self.fitness(population[j], self.n) <= pivot:
                i += 1
                population[i], population[j] = population[j], population[i]
        population[i+1], population[high] = population[high], population[i+1]

        return i + 1

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

        print("\n")
        for i in range(n):

            print("|", end='')
            for j in range(n):

                if queens[j] == i:
                    print(" x |", end='')

                else:
                    print("   |", end='')

            print("\n")