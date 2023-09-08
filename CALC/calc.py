class Calculator:
    history_array = None
    def __init__(self):
        self.history_array = []
    last_operation = None
    @property
    def last(self):
        return Calculator.last_operation


    def sum(self, a, b):
        '''
        
        '''
        self.history_array.append('sum({}, {}) == {}'.format(a, b, a + b))
        Calculator.last_operation = self.history_array[-1]
        return a + b
    

    def sub(self, a, b):
        '''
        
        '''
        self.history_array.append('sub({}, {}) == {}'.format(a, b, a - b))
        Calculator.last_operation = self.history_array[-1]
        return a - b
    

    def mul(self, a, b):
        '''
        
        '''
        self.history_array.append('mul({}, {}) == {}'.format(a, b, a * b))
        Calculator.last_operation = self.history_array[-1]
        return a * b
    

    def div(self, a, b, mod=False):
        '''
        
        '''
        if mod:
            self.history_array.append('div({}, {}) == {}'.format(a, b, a % b))
            Calculator.last_operation = self.history_array[-1]
            return a % b
        else:
            self.history_array.append('div({}, {}) == {}'.format(a, b, round((a / b),3)))
            Calculator.last_operation = self.history_array[-1]
            return a / b
        

    def pow(self, a,b):
        '''
        
        '''
        self.history_array.append('pow({}, {}) == {}'.format(a, b, a ** b))
        Calculator.last_operation = self.history_array[-1]
        return a ** b


    def history(self):
        try:
            result = self.history_array
        except IndexError:
            result = None
        return result
    
    
    def clear(self): 
        Calculator.last_operation = None

