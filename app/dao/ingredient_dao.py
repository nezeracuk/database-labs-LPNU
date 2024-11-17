from .. import db
from ..domain.ingredient import Ingredient

class IngredientDAO:
    @staticmethod
    def find_all():
        return Ingredient.query.all()

    @staticmethod
    def find_by_id(ingredient_id):
        ingredient = Ingredient.query.get(ingredient_id)
        if ingredient:
            db.session.refresh(ingredient)
        return ingredient

    @staticmethod
    def create(ingredient):
        db.session.add(ingredient)
        db.session.commit()
        return ingredient

    @staticmethod
    def create_all(ingredients):
        db.session.bulk_save_objects(ingredients)
        db.session.commit()
        return ingredients

    @staticmethod
    def update(ingredient_id, new_ingredient):
        ingredient = Ingredient.query.get(ingredient_id)
        if ingredient:
            for key, value in vars(new_ingredient).items():
                if key != 'id' and value is not None:
                    setattr(ingredient, key, value)
            db.session.commit()
        return ingredient

    @staticmethod
    def patch(ingredient_id, updates):
        ingredient = Ingredient.query.get(ingredient_id)
        if ingredient:
            for key, value in updates.items():
                setattr(ingredient, key, value)
            db.session.commit()
        return ingredient

    @staticmethod
    def put(ingredient_id, new_data):
        ingredient = Ingredient.query.get(ingredient_id)
        if ingredient:
            for key in vars(ingredient):
                if key != 'id':
                    setattr(ingredient, key, new_data.get(key, None))
            db.session.commit()
        return ingredient

    @staticmethod
    def delete(ingredient_id):
        ingredient = Ingredient.query.get(ingredient_id)
        if ingredient:
            db.session.delete(ingredient)
            db.session.commit()
            return True
        return False

    @staticmethod
    def delete_all():
        Ingredient.query.delete()
        db.session.commit()
