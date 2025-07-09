from server.usecase.users_usecase import usersUsecase 

class usersController:
    def __init__(self):
        self.user_usecase = usersUsecase()
        return
    
    def validate_login(self, username, password):
        return self.user_usecase.validate_login(username=username, password=password)
    
    def get_user_by_username(self, username):
        return self.user_usecase.get_user_by_username(username=username)
    
    def signup_user(self, name, username, email, password):
        return self.user_usecase.signup_user(name, username, email, password)