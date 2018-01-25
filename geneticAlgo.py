import geneticOperators
import random
from Class import Parser

def random_chromo(size):
    chromosome = ""
    for x in range(0,size):
        chromosome += str(random.randint(0,1))
    return chromosome












if __name__ == '__main__':
    import Main as Main
    Main.main()
