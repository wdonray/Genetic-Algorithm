import os
import sys
from Class import Parser
import geneticOperators
import geneticAlgo
def main():
    '''Main'''
    input1 = '(D+C)*(!O+B)'
    test = Parser(input1)
    print test.get_variables()
    print test.get_amount_clause()

    test.get_data_from_file('data.txt')
    print test.get_variables()
    print test.get_amount_clause()
    print ""
    chromosomes = '010101'
    chromosomes2 = '101010'
    print "Mom: " + str(chromosomes) + " Dad: " + str(chromosomes2)
    print "Mutate Mom: " + str(geneticOperators.mutate(chromosomes)) + " Mutate Dad: " + str(geneticOperators.mutate(chromosomes2))
    print "CrossOver: " + str(geneticOperators.crossover(chromosomes, chromosomes2, str(chromosomes).__len__() / 2))

if __name__ == "__main__":
    main()
