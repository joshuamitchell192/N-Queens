
class HillClimbing:
    '''Explore the state space by selecting the immediate neighbour
    with the minimal cost until no immediate neighbour improves the
    current cost.'''
    def __init__(self, queens, n, iterations):
        self.queens = queens
        self.n = n
        self.printBoard(queens, n)
        for i in range(iterations):
            if self.cost(queens, n) != 0:
                self.queens = self.neighbourEval(queens, n)
        print(queens)


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

                        if minCost == 0:
                            queens[bestColumn] = bestRow
                            return queens
            queensTemp = queens[:]
        queens[bestColumn] = bestRow
        print("Board: ", minCost)
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
        for i in range(n):
            for j in range(n):
                if queens[i] == j:
                    print("x")
                else: print(" ")
            print("\n")