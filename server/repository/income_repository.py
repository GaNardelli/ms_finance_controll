from sqlalchemy import Column, Date, ForeignKey, insert, text, update
from db_file import db

class Incomes(db.Model):
    __tablename__ = "incomes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    category = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255))
    value = db.Column(db.Float, nullable=False)
    create_time = db.Column(Date)
    received_date = db.Column(Date)

    def __repr__ (self):
        return f'IcomeID: {self.id}, UserId: {self.user_id}, Category: {self.category}, Description: {self.description}'
    
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
    def get_income_list (cls): 
        incomes = db.session.query(cls).all()
        return [income.to_dict() for income in incomes]

    @classmethod
    def create_new_income(cls, user, value, description, date, category, create_time):
        try:
            new_income = cls(
                user_id=user,
                value=value,
                description=description,
                received_date=date,
                create_time = create_time,
                category=category
            )
            db.session.add(new_income)
            db.session.commit()
            return {'statusCode': 201, 'msg': 'Income created successfully.'}
        except Exception as e:
            db.session.rollback()
            print(f"Error creating income: {e}")
            return {'statusCode': 500, 'msg': 'An error occurred while creating the income.'}

    @classmethod
    def remove_income(cls, income_id):
        try:
            income_to_remove = db.session.get(cls, income_id)
            if not income_to_remove:
                return {'statusCode': 404, 'msg': 'Income not found.'}
            db.session.delete(income_to_remove)
            db.session.commit()
            return {'statusCode': 200, 'msg': 'Income removed successfully.'}
        except Exception as e:
            db.session.rollback()
            print(f"Error removing income: {e}")
            return {'statusCode': 500, 'msg': 'An error occurred while removing the income.'}
        
    @classmethod
    def update_income(cls, income_id, value=None, description=None, date=None, category=None):
        try:
            income_to_update = db.session.get(cls, income_id)
            if not income_to_update:
                return {'statusCode': 404, 'msg': 'Income not found.'}
            update_income = (update(cls).where(cls.id==income_id))
            fields_to_update = {'value': value, 'description': description, 'received_date': date, 'category': category}
            for field, val in fields_to_update.items():
                if val is not None:
                    update_income = update_income.values(**{field: val})
            db.session.execute(update_income)
            db.session.commit()
            return {'statusCode': 200, 'msg': 'Income updated successfully.'}
        except Exception as e:
            db.session.rollback()
            print(f"Error updating income: {e}")
            return {'statusCode': 500, 'msg': 'An error occurred while updating the income.'}