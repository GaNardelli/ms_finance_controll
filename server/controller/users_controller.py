from server.usecase.users_usecase import usersUsecase 

class usersController:
    def __init__(self):
        self.user_usecase = usersUsecase()
        return
    
    def get_user_by_username(self, username):
        return 