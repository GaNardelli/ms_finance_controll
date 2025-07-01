from server.repository.income_repository import Incomes
import datetime

class incomeUsecase: 
    def __init__ (self):
        self.income_list = []
        self.date_string = "%Y-%m-%d %H:%M:%S"
    
    def get_income_list(self, id=None):
        get_list = Incomes.get_income_list()
        self.income_list = get_list
        return self.income_list
    
    def create_income(self, user, value, description, date, category):
        required_fields = {'User': user, 'Value': value, 'Description': description, 'Date': date, 'Category': category}
        for field, val in required_fields.items():
            if not val:
                return {'statusCode': 400, 'msg': f'{field} is required'}
            
        create_time = datetime.datetime.now()
        
        try:
            format_time = datetime.datetime.strptime(date, self.date_string)
        except ValueError:
            return {'statusCode': 400, 'msg': 'Invalid date format. Please use YYYY-MM-DD HH:MM:SS.'}
        
        return Incomes.create_new_income(user=user, value=value, description=description, date=format_time, category=category, create_time=create_time)
    
    def remove_income(self, income_id):
        if not income_id:
            return {'statusCode': 400, 'msg': f'Income ID is required'}
        return Incomes.remove_income(income_id)
        
        
