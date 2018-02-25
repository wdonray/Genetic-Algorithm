import geneticOperators
import random
from CNF import CNF
import math
class Chromosome(object):
    def __init__(self):
        self.id = ""
        self.fitness = 0
        self.fitness_ratio = 0
        self.minRange = 0
        self.maxRange = 0

    def display(self):
        print("Chromosome", self.id)
        print("Fitness", self.fitness)
        print("Fitness Ratio", self.fitness_ratio)

    def evalFitness(self, cnf):
        self.fitness = 0
        p = CNF(cnf)
        for i in p.string_data:
            self.fitness += 1
    
    def setFitnessRatio(self, score):
        self.fitness_ratio = round(self.fitness / score, 3)

    def setFitnessRange(self, chrom):
        self.minRange = round(chrom, 2)
        self.maxRange = round(self.fitness_ratio + chrom, 3)
        if(self.maxRange >= .99):
            self.maxRange = math.ceil(self.maxRange)
    
if __name__ == '__main__':
    import Main as Main
    Main.main()
