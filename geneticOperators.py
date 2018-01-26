import random
from Class import Parser

def mutate(chromosome):
    storage = ""
    for a in chromosome:
        ran = random.uniform(0,1)
        if ran < .5:
            if a is '0':
                a = '1'
            else:
                a = '0'
        storage += a
    return storage

def crossover(mom, dad, pivot):
    childA, childB = "" , ""
    for x in range(0, str(mom).__len__()):
        if x < pivot:
            childA += mom[x]
            childB += dad[x]
        else:
            childB += mom[x]
            childA += dad[x]
    return (childA, childB)

def calc_fitness(pop, cnf):
    p = Parser(cnf)
    p.get_clauses()
    p.get_amount_clause()
    p.get_variables()
    fitness = []




if __name__ == '__main__':
    import Main as Main
    Main.main()
