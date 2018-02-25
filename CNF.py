import random
'''Parser'''

class CNF(object):
    '''Parser'''

    def __init__(self, expression):
        self.string_data = expression
        self.num_clauses = 0
        self.variables = []
        self.storage = []
        self.grammar = ['*', '(', '+', ')', '!', '|', '^', '~']

    def get_variables(self):
        '''Get Variables'''
        test = []
        self.variables = self.string_data
        for i in self.grammar:
            self.variables = self.variables.replace(i, '')

        for data in self.variables:
            #Check for duplicates
            if data not in test:
                test.append(data)

        self.variables = sorted(test, key=lambda x: x)
        return self.variables

    def get_data_from_file(self, filename):
        '''Get Data From File'''
        test_file = open(filename, 'ab+')
        self.string_data = test_file.read()

    def get_amount_clause(self):
        '''Get Clause Amount'''
        self.num_clauses = 0
        for data in self.string_data:
            if data is '(':
                self.num_clauses += 1
        return 'Clause Amount: ' + str(self.num_clauses)

    def get_clauses(self):
        self.storage = []
        copy = False
        add_string = ""
        for x in self.string_data:
            if x is '(':
                copy = True
            if copy:
                add_string += x
            if x is ')':
                copy = False
                self.storage.append(add_string)
                add_string = ''
        return self.storage

    def change(self):
        new = ''
        for x in self.storage:
            for c in x:
                if c is '+':
                    new += '|'
                elif c is '!':
                    new += '~'
                elif c is '*':
                    new += '^'
                else:
                    new += c
        self.string_data = new
        self.get_variables()
        self.get_clauses()
        self.get_amount_clause()

    def test_solution(self, solution):
        result = []
        variables = {}
        self.change()
        i = 0
        for v in self.variables:
            variables[v] = solution[i]
            i += 1
        clauses = self.storage
        for c in clauses:
            clauseval = ''
            for place in range(1, str(c).__len__()-1):
                if c[place] in self.variables:
                    clauseval += variables[c[place]]
                else:
                    clauseval += c[place]
            result.append(eval(clauseval))    
        fixedResult = []
        for r in result:
            if r is -1:
                fixedResult.append(1)
            elif r is -2:
                fixedResult.append(0)
            else:
                fixedResult.append(r)
        return fixedResult    

if __name__ == '__main__':
    import Main as Main
    Main.main()
