import random
import geneticOperators
from CNF import CNF
from Chromosome import Chromosome


def randomChromo(size):
    chro = Chromosome()
    for i in range(0, size):
        chro.id += str(random.randint(0, 1))
    return chro



def geneticFunction(cnf):
    p = CNF(cnf)
    p.get_variables()
    population = []
    generation = 1

    population.append(randomChromo(p.storage.__len__()))
    print population
    print("Solving for ", cnf)
    while True:
        fitnessess = geneticOperators.fitnessFunc(population, cnf)
        newpop = []
        for i in range(0, population.__len__()-1):
            children = geneticOperators.crossover(population[i], population[i + 1])
            child1 = geneticOperators.mutate(children[0])
            child2 = geneticOperators.mutate(children[1])

            newpop.append(children1)
            newpop.append(children2)
            i += 1
        population = newpop
        generation += 1

        