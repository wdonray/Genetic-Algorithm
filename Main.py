import os
import sys
from CNF import CNF
import geneticOperators
import geneticAlgorithm


def main():
    '''Main'''
    print "<======================================================================>\n"
    testOne = CNF('')
    testOne.get_data_from_file('TestOne.txt')
    print "Solving For: " + testOne.string_data
    print testOne.get_amount_clause()
    print "Expected: All values must evaluate to true except for second one" 
    solutionOne = str(geneticAlgorithm.geneticFunction(testOne.string_data))
    print "Solution One " + solutionOne + "\n"
    print "<======================================================================>\n"

    testTwo = CNF('')
    testTwo.get_data_from_file('TestTwo.txt')
    print "Solving For: " + testTwo.string_data
    print testTwo.get_amount_clause()
    print "Expected: First half True and second half false" 
    solutionTwo = str(geneticAlgorithm.geneticFunction(testTwo.string_data))
    print "Solution Two " + solutionTwo + "\n"
    print "<======================================================================>\n"

    testThree = CNF('')
    testThree.get_data_from_file('TestThree.txt')
    print "Solving For: " + testThree.string_data
    print testThree.get_amount_clause()
    print "Expected: All true except for last three" 
    solutionThree = str(geneticAlgorithm.geneticFunction(testThree.string_data))
    print "Solution Three " + solutionThree + "\n"
    print "<======================================================================>\n"
    
    testFour = CNF('')
    testFour.get_data_from_file('TestFour.txt')
    print "Solving For: " + testFour.string_data
    print testFour.get_amount_clause()
    print "Expected: All true expect for first two" 
    solutionFour = str(geneticAlgorithm.geneticFunction(testFour.string_data))
    print "Solution Four " + solutionFour + "\n"
    print "<======================================================================>\n"
    
    raw_input()
if __name__ == "__main__":
    main()
