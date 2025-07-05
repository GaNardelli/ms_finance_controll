from server.repository.expense_repository import Expenses
import datetime

class expenseUsecase:
    def __init__(self):
        self.expense_list = []
        self.date_string = "%Y-%m-%d %H:%M:%S"

    def get_expense_list(self, id=None):
        get_list = Expenses.get_expense_list()
        self.expense_list = get_list
        return self.expense_list
    
    def create_expense(self, user, value, description, date, category, is_fixed=0):
        required_fields = {'User': user, 'Value': value, 'Description': description, 'Date': date, 'Category': category}
        for field, val in required_fields.items():
            if not val:
                return {'statusCode': 400, 'msg': f'{field} is required'}
        created_time = datetime.datetime.now()

        try:
            format_time = datetime.datetime.strptime(date, self.date_string)
        except ValueError:
            return {'statusCode': 400, 'msg': 'Invalid date format. Please use YYYY-MM-DD HH:MM:SS.'}
        
        return Expenses.create_new_expense(user=user, value=value, description=description, date=format_time, category=category, created_time=created_time, is_fixed=is_fixed)
    
    def remove_expense(self, id):
        if not id:
            return {'statusCode': 400, 'msg': f'Income ID is required'}
        return Expenses.delete_expense(id)
    
    def update_expense(self, id, value=None, description=None, date=None, category=None, is_fixed=None):
        required_fields = {'Income ID': id}
        for field, val in required_fields:
            if not val:
                return {'statusCode': 400, 'msg:': f'{field} is required.'}
            
        if date:
            try:
                date = datetime.datetime.strptime(date, self.date_string)
            except ValueError:
                return {'statusCode': 400, 'msg': 'Invalid date format. Please use YYYY-MM-DD HH:MM:SS.'}
            
        return Expenses.update_expense(id, value, description, date, category, is_fixed)