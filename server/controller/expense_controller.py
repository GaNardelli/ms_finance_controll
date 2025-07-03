from server.usecase.expense_usecase import expenseUsecase

class expenseController:
    def __init__(self):
        self.expense_usecase = expenseUsecase()
        return
    
    def get_expense_list(self, id = None):
        return self.expense_usecase.get_expense_list(id)
    
    def create_expense(self, user, value, description, date, category):
        return self.expense_usecase.create_expense(user, value, description, date, category)
    
    def remove_expense(self, income_id):
        return self.expense_usecase.remove_expense(income_id)
    
    def update_expense(self, income_id, value=None, description=None, date=None, category=None):
        return self.expense_usecase.update_expense(income_id, value, description, date, category)