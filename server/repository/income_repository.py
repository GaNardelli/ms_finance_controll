from sqlalchemy import Column, Date, ForeignKey
from app import db

class Incomes(db.Model):
    __tablename__ = "incomes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)
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
    def insert_income (cls, user_id, category, description, value, create_time, recived_date) :
        pass