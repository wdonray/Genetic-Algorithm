import random
from CNF import CNF
from Chromosome import Chromosome


def mutate(chromosome):
    storage = ""
    for a in chromosome:
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
    for x in range(0, str(mom).__len__()):
        if x < pivot:
            childA += mom[x]
            childB += dad[x]
        else:
            childB += mom[x]
            childA += dad[x]
    return (childA, childB)


def fitnessFunc(pop, cnf):
    p = CNF(cnf)
    p.get_clauses()
    p.get_amount_clause()
    p.get_variables()
    p.change()
    score = 0
    count = 0
    for i in pop:
        i.id = str(count)
        i.evalFitness(p)
        score += i.fitness
        count += 1

    prev = 0
    for x in pop:
        x.setFitnessRatio(score)
        x.setFitnessRange(prev)
        prev = x.maxRange
    return pop



if __name__ == '__main__':
    import Main as Main
    Main.main()
