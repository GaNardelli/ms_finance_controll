from server.usecase.categories_usecase import categoriesUsecase


class categoriesController:
    def __init__(self):
        self.categories_usecase = categoriesUsecase()
        return
    
    def get_category_list(self, user, id=None):
        return self.categories_usecase.get_category_list(id=id, user=user)
    
    def create_category(self, user, description=None, generic=None):
        return self.categories_usecase.create_category(user, description, generic)
    
    def update_category(self, id, user, description=None, generic=None):
        return self.categories_usecase.update_category(id, user, description, generic)
    
    def delete_category(self, id):
        return self.categories_usecase.delete_category(id)