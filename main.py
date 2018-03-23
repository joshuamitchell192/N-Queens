from HillClimbing import HillClimbing
from RandomRestartHC import RandomRestartHC
from SimulatedAnnealing import SimulatedAnnealing
from Genetic import Genetic

from RandomRestartHCExperiment import RandomRestartHCExperiment
from SimulatedAnnealingExperiment import SimulatedAnnealingExperiment
from GeneticExperiment import GeneticExperiment
import numpy as np
# TODO - Comment Code

# Performance Improvements
# TODO - Tournament Selection
# TODO -

from random import randint
n = int(input("What is the number of queens: "))

while n < 4 :
    print("Solution cannot be found for a number less than 4.\nEnter another number")
    n = int(input("What is the number of queens: "))
print("\n1. Hill Climbing\n2. Random Restart Hill Climbing\n3. Simulated Annealing\n4. Genetic\n")
algorithm = int(input("Select which algorithm you would like to use: "))

queens = list([randint(0, n - 1) for x in range(n)])
#print(queens)

if algorithm == 1:

    result = HillClimbing(queens, n, 200)

elif algorithm == 2:

    result = RandomRestartHCExperiment(queens, n, int(np.log(n**7)))

elif algorithm == 3:

    result = SimulatedAnnealingExperiment(queens, n)

elif algorithm == 4:

    result = Genetic(n)



