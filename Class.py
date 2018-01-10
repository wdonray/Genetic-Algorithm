class Parser(object):
    '''Parser'''

    def __init__(self, string):
        self.string_data = string

    def get_variables(self):
        storage = []
        i = 0
        for data in self.string_data:
            if data is '(' or data is '+':
                
                if self.string_data[i+1] is '!':
                    
                    if (self.string_data[i+2],) not in storage:
                        
                        storage.append((self.string_data[i+2],))
                        
                elif (self.string_data[i+1],) not in storage:
                    
                    storage.append((self.string_data[i+1],))
            i+=1
        print storage

    def get_data_from_file(self, filename):
        test_file = open(filename, 'ab+')
        self.string_data = test_file.read()

if __name__ == '__main__':
    import Main as Main
    Main.main()

