import random
from CNF import CNF
import math
class Chromosome(object):
    def __init__(self):
        self.id = ""
        self.fitness = 0
        self.fitness_ratio = 0

    def __str__(self):
        return "Chromosome: " + str(self.id) + " Fitness: " + (str(round(self.fitness,2)))

    def evalFitness(self, cnf):
        self.fitness = 0
        p = CNF(cnf)
        p.get_amount_clause()
        p.get_clauses()
        p.get_variables()
        result = p.test_solution(self.id)
        for s in result:
            if s is 1:
                self.fitness += 1
        self.fitness = float(self.fitness)/float(p.num_clauses)

    
if __name__ == '__main__':
    import Main as Main
    Main.main()
