from random import randint
import time


class RandomRestartHC:
    '''Explore the state space by selecting the immediate neighbour
    with the minimal cost. If no neighbour improves the current cost,
    restart with a new random set of queen positions.'''

    def __init__(self, queens, n, iterations):

        self.queens = queens
        self.n = n
        self.iterations = iterations
        self.printBoard(self.queens, n)

        Attempts = 0
        cost = 0
        stat = []
        start = time.time()

        # Restart and continue search until a solution is found
        while self.cost(self.queens, n) != 0:
            # Increment Attempts to track number of restarts
            Attempts += 1

            # Initialise queens to random state
            self.queens = list([randint(0, n - 1) for x in range(n)])

            # Select new best moves and for a certain number of iterations
            for i in range(self.iterations):

                # if the cost != 0 then select another move
                cost = self.cost(self.queens, n)
                stat.append(cost)

                if cost != 0:
                    self.neighbourEval(self.queens, n)

            print(self.queens)
        print('\n', stat)
        end = time.time()
        # if cost = 0, print board and other information
        self.printBoard(self.queens, n)
        print("Runtime:", end-start, "(seconds)")
        print("Attempts:", Attempts)

    def neighbourEval(self, queens, n):
        """find the best move for the current board state"""
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

    def cost(self, queens, n):
        """
        Calculates the cost by counting the number of queen conflicts
        """

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
        """
        Prints out the board with the queens array.
        """
        print("\n")
        for i in range(n):

            print("|", end='')
            for j in range(n):

                if queens[j] == i:
                    print(" x |", end='')

                else:
                    print("   |", end='')

            print("\n")

