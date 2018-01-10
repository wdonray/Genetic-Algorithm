import os
import sys
from Class import Parser


def main():
    '''Main'''
    input1 = '(D+C)*(!O+B)'
    test = Parser(input1)
    print test.get_variables()
    print test.get_amount_clause()

    test.get_data_from_file('data.txt')
    print test.get_variables()
    print test.get_amount_clause()


if __name__ == "__main__":
    main()
