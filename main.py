from HillClimbing import HillClimbing
from RandomRestartHC import RandomRestartHC
from SimulatedAnnealing import SimulatedAnnealing


from random import randint
n = int(input("What is the number of queens: "))
print("\n1. Hill Climbing\n2. Random Restart Hill Climbing\n3. Simulated Annealing\n4. Genetic")
algorithm = int(input("Select which algorithm you would like to use: "))

queens = [randint(0, n-1) for x in range(n)]
print(queens)
if algorithm == 1:
    result = HillClimbing(queens, n, 200)
elif algorithm == 2:
    result = RandomRestartHC(queens, n, n)
elif algorithm == 3:
    result = SimulatedAnnealing(queens, n)
elif algorithm == 4:
    result = 0


