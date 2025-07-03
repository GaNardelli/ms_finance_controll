from sqlalchemy import Column, Date, ForeignKey, insert, text, update
from app import db

class Expense(db.Model):
    __tablename__ = "expenses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False) 
    value = db.Column(db.Float, nullable=False)
    category = db.Column(db.Integer, nullable=False)
    expense_date = db.Column(Date)
    description = db.Column(db.String(255))
    created_time = db.Column(Date)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'category': self.category,
            'description': self.description,
            'value': self.value,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'received_date': self.received_date.isoformat() if self.received_date else None,
        }

    @classmethod
    def get_expense_list(cls):
        expenses = db.session.query(cls).all()
        return [expense.to_dict() for expense in expenses]
    
    @classmethod
    def create_new_expense(cls, user, value, description, date, category, create_time):
        try:
            new_expense = cls(
                user_id = user,
                value = value,
                description = description,
                expense_date = date,
                create_time = create_time,
                category = category
            )
            db.session.add(new_expense)
            db.session.commit()
            return {'statusCode': 200, 'msg': 'Expense created successfully.'}
        except Exception as e:
            db.session.rollback()
            print(f"Error creating expense: {e}")
            return {'statusCode': 500, 'msg': 'An error occurred while creating the expense.'}
        
    @classmethod
    def delete_expense(cls, expense_id):
        try:
            expense_to_delete = db.session.get(cls, expense_id)
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
    def update_expense(cls, expense_id, value=None, description=None, date=None, category=None):
        try:
            expense_to_update = db.session.get(cls, expense_id)
            if not expense_to_update:
                return {'statusCode': 404, 'msg': 'Expense not found.'}
            fields_to_update = {'value': value, 'description': description, 'expense_date': date, 'category': category}
            update_expense = (update(cls).where(cls.id == expense_id))
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
        



