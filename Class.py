'''Parser'''

class Parser(object):
    '''Parser'''

    def __init__(self, expression):
        self.string_data = expression
        self.num_clauses = 0
        self.storage = []
        self.grammar = ['!', '+', '*', '(', ')']

    def get_variables(self):
        '''Get Variables'''
        test = []
        self.storage = self.string_data
        for i in self.grammar:
            self.storage = self.storage.replace(i, '')

        for data in self.storage:
            #Check for duplicates
            if data not in test:
                test.append(data)

        self.storage = sorted(test, key = lambda x: x)
        return self.storage

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


if __name__ == '__main__':
    import Main as Main
    Main.main()
