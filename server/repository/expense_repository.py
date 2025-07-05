from sqlalchemy import Column, Date, ForeignKey, insert, text, update
from db_file import db

class Expenses(db.Model):
    __tablename__ = "expenses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False) 
    value = db.Column(db.Float, nullable=False)
    category = db.Column(db.Integer, nullable=False)
    is_fixed = db.Column(db.Boolean, default=False)
    expense_date = db.Column(db.DateTime)
    description = db.Column(db.String(255))
    created_time = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'category': self.category,
            'description': self.description,
            'value': self.value,
            'is_fixed': self.is_fixed,
            'created_time': self.created_time.isoformat() if self.created_time else None,
            'expense_date': self.expense_date.isoformat() if self.expense_date else None,
        }

    @classmethod
    def get_expense_list(cls):
        expenses = db.session.query(cls).all()
        return [expense.to_dict() for expense in expenses]
    
    @classmethod
    def create_new_expense(cls, user, value, description, date, category, created_time, is_fixed=0):
        try:
            new_expense = cls(
                user_id = user,
                value = value,
                description = description,
                expense_date = date,
                created_time = created_time,
                category = category,
                is_fixed = is_fixed
            )
            db.session.add(new_expense)
            db.session.commit()
            return {'statusCode': 200, 'msg': 'Expense created successfully.'}
        except Exception as e:
            db.session.rollback()
            print(f"Error creating expense: {e}")
            return {'statusCode': 500, 'msg': 'An error occurred while creating the expense.'}
        
    @classmethod
    def delete_expense(cls, id):
        try:
            expense_to_delete = db.session.get(cls, id)
            if not expense_to_delete:
                return {'statusCode' : 404, 'msg': 'Expense not found.'}
            db.session.delete(expense_to_delete)
            db.session.commit()
            return {'statusCode' : 200, 'msg': 'Expense deleted successfully.'}
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting expense: {e}")
            return {'statusCode': 500, 'msg': 'An error occurred while deleting the expense.'}
        
    @classmethod
    def update_expense(cls, id, value=None, description=None, date=None, category=None, is_fixed=None):
        try:
            expense_to_update = db.session.get(cls, id)
            if not expense_to_update:
                return {'statusCode': 404, 'msg': 'Expense not found.'}
            is_fixed_boolean = True if int(is_fixed) == 1 else False
            fields_to_update = {'value': value, 'description': description, 'expense_date': date, 'category': category, 'is_fixed': is_fixed_boolean}
            update_expense = (update(cls).where(cls.id == id))
            for field, val in fields_to_update.items():
                if val is not None:
                    update_expense = update_expense.values(**{field: val})
            db.session.execute(update_expense)
            db.session.commit()
            return {'statusCode': 200, 'msg': 'Expense updated successfully.'}
        except Exception as e:
            db.session.rollback()
            print(f"Error updating expense: {e}")
            return {'statusCode': 500, 'msg': 'An error occurred while updating the expense.'}
        
