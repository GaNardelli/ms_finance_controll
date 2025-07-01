class incomeUsecase: 
    def __init__ (self):
        self.incomeList = [{
            'description': 'Salary',
            'value': 3000,
            'id': 0
            },{
            'description': 'Bonus',
            'value': 400,
            'id': 1
            }]
    
    def getInitList(self, id=None):
        return self.incomeList