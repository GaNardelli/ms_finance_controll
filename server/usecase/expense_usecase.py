from server.repository.expense_repository import Expense
import datetime

class expenseUsecase:
    def __init__(self):
        self.expense_list = []
        self.date_string = "%Y-%m-%d %H:%M:%S"

    def get_expense_list(self, id=None):
        get_list = Expense.get_expense_list()
        self.expense_list = get_list
        return self.expense_list
    
    def create_expense(self, user, value, description, date, category):
        required_fields = {'User': user, 'Value': value, 'Description': description, 'Date': date, 'Category': category}
        for field, val in required_fields.items():
            if not val:
                return {'statusCode': 400, 'msg': f'{field} is required'}
        create_time = datetime.datetime.now()

        try:
            format_time = datetime.datetime.strptime(date, self.date_string)
        except ValueError:
            return {'statusCode': 400, 'msg': 'Invalid date format. Please use YYYY-MM-DD HH:MM:SS.'}
        
        return Expense.create_expense(user=user, value=value, description=description, date=format_time, category=category, create_time=create_time)
    
    def remove_expense(self, income_id):
        if not income_id:
            return {'statusCode': 400, 'msg': f'Income ID is required'}
        return Expense.delete_expense(income_id)
    
    def update_expense(self, income_id, value=None, description=None, date=None, category=None):
        required_fields = {'Income ID': income_id}
        for field, val in required_fields:
            if not val:
                return {'statusCode': 400, 'msg:': f'{field} is required.'}
            
        if date:
            try:
                date = datetime.datetime.strptime(date, self.date_string)
            except ValueError:
                return {'statusCode': 400, 'msg': 'Invalid date format. Please use YYYY-MM-DD HH:MM:SS.'}
            
        return Expense.update_expense(income_id, value, description, date, category)