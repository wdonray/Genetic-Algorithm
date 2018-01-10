import os
import sys
from Class import Parser

def main():
    test = Parser('(D+C)*(!O+B)')
    test.get_variables()

    test.get_data_from_file('data.txt')
    test.get_variables()


if __name__ == "__main__":
    main()