from sqlalchemy import func, select
from db_file import db

class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

    @classmethod
    def get_user_by_username(cls, username):
        users = select(cls).where(func.upper(cls.username)==func.upper(username))
        result = db.session.execute(users).scalars().all()
        return [user.to_dict() for user in result]
    
    @classmethod
    def singup_user(cls, name, username, email, password, created_at):
        try:
            new_user = cls(
                name=name,
                username=username,
                email=email,
                password_hash=password,
                created_at=created_at
            )
            db.session.add(new_user)
            db.session.commit()
            return {'statusCode': 200, 'msg': 'User created successfully.'}
        except Exception as e:
            db.session.rollback()
            print(f"Error creating user: {e}")
            return {'statusCode': 500, 'msg': 'An error occurred while creating the User.'}