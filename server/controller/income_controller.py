from server.usecase.income_usecase import incomeUsecase

class incomeController: 
    def __init__(self):
        self.income_usecase = incomeUsecase()
        return
    
    def getIncomesList(self, id = None):
        return self.income_usecase.getInitList(id)