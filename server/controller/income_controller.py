from server.usecase.income_usecase import incomeUsecase

class incomeController: 
    def __init__(self):
        self.income_usecase = incomeUsecase()
        return
    
    def get_income_list(self, id = None):
        return self.income_usecase.get_income_list(id)
    
    def create_income(self, user, value, description, date, category):
        return self.income_usecase.create_income(user, value, description, date, category)
    
    def remove_income(self, income_id):
        return self.income_usecase.remove_income(income_id)
    
    def update_income(self, income_id, value=None, description=None, date=None, category=None):
        return self.income_usecase.update_income(income_id, value, description, date, category)