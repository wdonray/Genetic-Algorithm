import os
import sys
from CNF import CNF
import geneticOperators
import geneticAlgorithm


def main():
    '''Main'''
    p = CNF('(A+B)*(B+!C)')
    p.get_data_from_file('data.txt')

    print str(geneticAlgorithm.geneticFunction(p.string_data))
    raw_input()
if __name__ == "__main__":
    main()
