import os
import sys
from CNF import CNF
import geneticOperators
import geneticAlgorithm


def main():
    '''Main'''
    p = CNF('')
    p.get_data_from_file('data.txt')

    solution = str(geneticAlgorithm.geneticFunction(p.string_data))
    print ("Solution", solution)
    raw_input()
if __name__ == "__main__":
    main()
