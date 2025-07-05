from server.usecase.expense_usecase import expenseUsecase

class expenseController:
    def __init__(self):
        self.expense_usecase = expenseUsecase()
        return
    
    def get_expense_list(self, id = None):
        return self.expense_usecase.get_expense_list(id)
    
    def create_expense(self, user, value, description, date, category, is_fixed=0):
        return self.expense_usecase.create_expense(user, value, description, date, category, is_fixed=is_fixed)
    
    def remove_expense(self, id):
        return self.expense_usecase.remove_expense(id)
    
    def update_expense(self, id, value=None, description=None, date=None, category=None, is_fixed=None):
        return self.expense_usecase.update_expense(id, value, description, date, category, is_fixed)