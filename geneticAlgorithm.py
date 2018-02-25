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
    p.get_clauses()
    p.get_amount_clause()
    p.get_variables()
    p.change()
    population = []
    population.append(randomChromo(p.storage.__len__()))
    population.append(randomChromo(p.storage.__len__()))
    print("Solving for ", cnf)
    while True:
        fitnessess = geneticOperators.fitnessFunc(population, cnf)
        x = 0
        for c in population:
            c.fitness = fitnessess[x].fitness
            print c
            x += 1
        for c in population:
            if int(c.fitness) is 1:
                print("solved")
                return
        newpop = []
        for i in range(0, population.__len__()-1):
            num = random.randint(0, population[0].id.__len__())
            children = geneticOperators.crossover(population[i], population[i + 1], num)
            child1 = Chromosome()
            child2 = Chromosome()
            child1.id = geneticOperators.mutate(children[0])
            child2.id = geneticOperators.mutate(children[1])

            newpop.append(child1)
            newpop.append(child2)
            i += 1
        population = newpop
if __name__ == '__main__':
    import Main as Main
    Main.main()
