from random import randint
import time
import matplotlib.pyplot as plt
from multiprocessing import Pool


class RandomRestartHCExperiment:
    '''Explore the state space by selecting the immediate neighbour
    with the minimal cost. If no neighbour improves the current cost,
    restart with a new random set of queen positions.'''

    def __init__(self, queens, n, iterations):
        self.queens = queens
        self.n = n
        self.iterations = iterations
        #self.printBoard(self.queens, n)

        p = Pool()
        r = p.apply_async(self.mainMeth, range(4, n + 1))
        average = r.get()

        p.close()
        p.join()
        '''runtimeStat = []
        runtimeStat.append(average)'''
        xaxis = [i for i in range(4, n + 1)]
        plt.plot(xaxis, average, color='black', linestyle='dotted')
        plt.xlabel('Number of Queens')
        plt.ylabel('Runtime')
        plt.title('Simulated Annealing')
        plt.show()

    def mainMeth(self, i):
        runtime = []


        sum = 0
        average = 0
        n = i
        self.queens[:] = list([randint(0, n - 1) for x in range(n)])
        for j in range(20):
            Attempts = 0
            start = time.time()
            while self.cost(self.queens, n) != 0:
                Attempts += 1
                self.queens = list([randint(0, n - 1) for x in range(n)])

                for x in range(self.iterations):
                    if self.cost(self.queens, n) != 0:
                        self.neighbourEval(self.queens, n)
                print(self.queens)
            end = time.time()
            runtime.append((end - start))
            # self.printBoard(self.queens, n)
            # print("Runtime:", end - start, "(seconds)")
            # print("Attempts:", Attempts)
            self.queens[:] = list([randint(0, n - 1) for x in range(n)])
        for x in range(len(runtime)):
            sum += runtime[x]
        average = sum / len(runtime)
        print(average)

        return average

    def neighbourEval(self, queens, n):

        queensTemp = queens[:]
        minCost = 2000
        # iterate through queens
        for i in range(n):
            # iterate through rows
            for j in range(n):
                # check if the queen is in the same position
                if j == queens[i]:
                    j = j + 1
                else:
                    # move queen to the next row
                    queensTemp[i] = j
                    # determine cost for current position
                    cost = self.cost(queensTemp, n)

                    if cost < minCost:
                        # store the best position and its cost so far
                        bestColumn = i
                        bestRow = j
                        minCost = cost

            queensTemp = queens[:]
        self.queens[bestColumn] = bestRow
        print("\r", "Cost:", minCost, end=' ', flush=True)
        # print(self.cost(queens, n))

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

