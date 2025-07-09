from datetime import datetime
import re
import bcrypt
from server.repository.users_repository import Users

class usersUsecase:
    def __init__(self):
        self.user_repository = Users()
        return
    
    def __hash_password(self, password):
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(password, salt)
        return hash_password
    
    def __compare_hash_password(self, entered_password, stored_password):
        if bcrypt.checkpw(entered_password, stored_password):
            return {'statusCode': 200, 'msg': 'Passwords match!'}
        else:
            return {'statusCode':401, 'msg': 'Passwords dont match!'}
        
    def __email_validator(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            return True
        else:
            return False
        
    def validate_login(self, username, password):
        user_refferece = self.user_repository.get_user_by_username(username=username)
        if len(user_refferece) <= 0:
            return {'statusCode': 404, 'msg':'Users doesent exists.'}
        compare_password = self.__compare_hash_password(entered_password=password.encode('utf-8'), stored_password=user_refferece[0].get('password_hash').encode('utf-8'))
        return compare_password
        
    def get_user_by_username(self, username):
        if not username:
            return {'statusCode': 404, 'msg':'Please insert a valid username.'}
        return self.user_repository.get_user_by_username(username=username)
    
    def signup_user(self, name, username, email, password):
        required_fields = {'Name': name, 'Username': username, 'Email': email, 'Password': password}
        password_hash = ''
        for field, val in required_fields.items():
            if not val:
                return {'statusCode':400, 'msg':f'Field {field} is required'}
            if field == 'Username':
                get_user = self.user_repository.get_user_by_username(username=username)
                if len(get_user) > 0:
                    return {'statusCode': 409, 'msg':'Username already exists.'}
            if field == 'Password':
                password_hash = self.__hash_password(password.encode('utf-8'))
            if field == 'Email':
                validate_email = self.__email_validator(email)
                if validate_email == False:
                    return {'statusCode': 422, 'msg': 'Please insert a valid email.'}
        created_at = datetime.now()
        return self.user_repository.singup_user(name=name, username=username, email=email, password=password_hash, created_at=created_at)
