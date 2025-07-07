from os import execle
from sqlalchemy import select, update
from db_file import db

class Categories(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255))
    generic = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'description': self.description,
            'generic': self.generic
        }
    
    @classmethod
    def get_category_list(cls, user, id=None):
        categories = db.session.query(cls).where(cls.user_id==user).all()
        return [category.to_dict() for category in categories]
    
    @classmethod
    def create_category(cls, user, description, generic=None):
        try:
            is_generic_boolean = True if int(generic) == 1 else False
            new_category = cls(
                user_id = user,
                description = description,
                generic = is_generic_boolean
            )
            db.session.add(new_category)
            db.session.commit()
            return {'statusCode': 200, 'msg': 'Category create successfully.'}
        except Exception as e:
            db.session.rollback()
            print(f'Error while creating the category {e}')
            return {'statusCode':500, 'msg':  'An error occurred while creating the category.'}
        
    @classmethod
    def update_category(cls, id, user, description, generic):
        try:
            if generic:
                is_generic_boolean = True if int(generic) == 1 else False
            update_category = (
                update(cls)
                .where(cls.id==id)
                .where(cls.user_id==user)
            )
            fields_to_update = {'description':description, 'generic': is_generic_boolean}
            for field, val in fields_to_update.items():
                if val is not None:
                    update_category = update_category.values(**{field: val})
            db.session.execute(update_category)
            db.session.commit()
            return {'statusCode':200, 'msg': 'Categroy updated successfully'}
        except Exception as e:
            db.session.rollback()
            print(f'Error while update category {e}')
            return {'statusCode':500, 'msg': 'An error occurred while updateing the category'}
        
    @classmethod
    def delete_category(cls, id):
        try:
            category_to_delete = db.session.get(cls, id)
            if not category_to_delete:
                return {'statusCode' : 404, 'msg': 'Category not found.'}
            db.session.delete(category_to_delete)
            db.session.commit()
            return {'statusCode' : 200, 'msg': 'Category deleted successfully.'}
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting category: {e}")
            return {'statusCode': 500, 'msg': 'An error occurred while deleting the category.'}