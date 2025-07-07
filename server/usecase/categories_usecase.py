from server.repository.categories_repository import Categories

class categoriesUsecase:
    def __init__(self):
        self.category_list = []
        return
    
    def get_category_list(self, user, id=None):
        if not user:
            return {'statusCode':400, 'msg':'Field User is required.'}
        get_list = Categories.get_category_list(user=user)
        self.category_list = get_list
        return self.category_list
    
    def create_category(self, user, description, generic):
        fields_to_update = {'UserID': user, 'Description': description, 'Generic': generic}
        for field, val in fields_to_update.items():
            if not val:
                return {'statusCode':404, 'msg': f'Field {field} is required.'}
        return Categories.create_category(user, description, generic)

    def update_category(self, id, user, description=None, generic=None):
        fields_to_update = {'ID': id, 'UserID': user}
        for field, val in fields_to_update.items():
            if not val:
                return {'statusCode':404, 'msg': f'Field {field} is required.'}
        return Categories.update_category(id, user, description, generic)
    
    def delete_category(self, id):
        if not id:
            return {'statusCode':404, 'msg': 'Category ID is required.'}
        return Categories.delete_category(id)