import time

class HillClimbing:
    '''Explore the state space by selecting the immediate neighbour
    with the minimal cost until no immediate neighbour improves the
    current cost.'''
    def __init__(self, queens, n, iterations):
        self.queens = queens
        self.n = n
        self.printBoard(self.queens, n)
        start = time.time()
        for i in range(iterations):
            if self.cost(self.queens, n) != 0:
                self.neighbourEval(self.queens, n)
        end = time.time()
        self.printBoard(self.queens, n)
        print("Runtime:", end - start, "(seconds)")
        print(self.queens)



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

            queensTemp = queens[:]
        queens[bestColumn] = bestRow


        print("\r", "Cost:", minCost, end=' ', flush=True)
        #print(self.cost(queens, n))

    def cost(self, queens, n):
        conflicts = 0

        for i in range(n):
            for j in range(i+1, n):
                if i != j:
                    #Horizontal axis
                    if queens[i] == queens[j]:
                        conflicts = conflicts + 1
                    #Diagonal Axis Positive
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