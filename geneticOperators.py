import random
from CNF import CNF
from Chromosome import Chromosome


def mutate(chromosome):
    storage = ""
    for a in chromosome.id:
        ran = random.uniform(0, 1)
        if ran < .5:
            if a is '0':
                a = '1'
            else:
                a = '0'
        storage += a
    return storage


def crossover(mom, dad, pivot):
    childA, childB = "", ""
    for x in range(0, str(mom.id).__len__()):
        if x < pivot:
            childA += mom.id[x]
            childB += dad.id[x]
        else:
            childB += mom.id[x]
            childA += dad.id[x]
    child1 = Chromosome()
    child2 = Chromosome()
    child1.id = childA
    child2.id = childB
    return (child1, child2)


def fitnessFunc(pop, cnf):
    p = CNF(cnf)
    score = 0
    for i in pop:
        i.evalFitness(cnf)
        score += i.fitness
    return pop

if __name__ == '__main__':
    import Main as Main
    Main.main()
