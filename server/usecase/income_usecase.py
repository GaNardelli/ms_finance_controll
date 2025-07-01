from server.repository.income_repository import Incomes

class incomeUsecase: 
    def __init__ (self):
        self.income_list
    
    def getInitList(self, id=None):
        get_list = Incomes.get_income_list()
        self.income_list = get_list
        return self.income_list