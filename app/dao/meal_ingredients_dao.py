from .. import db
from ..domain.meal_ingredients import MealIngredients

class MealIngredientsDAO:
    @staticmethod
    def find_all():
        return MealIngredients.query.all()

    @staticmethod
    def find_by_id(meal_ingredient_id):
        meal_ingredient = MealIngredients.query.get(meal_ingredient_id)
        if meal_ingredient:
            db.session.refresh(meal_ingredient)
        return meal_ingredient

    @staticmethod
    def create(meal_ingredient):
        db.session.add(meal_ingredient)
        db.session.commit()
        return meal_ingredient

    @staticmethod
    def create_all(meal_ingredients):
        db.session.bulk_save_objects(meal_ingredients)
        db.session.commit()
        return meal_ingredients

    @staticmethod
    def update(meal_ingredient_id, new_meal_ingredient):
        meal_ingredient = MealIngredients.query.get(meal_ingredient_id)
        if meal_ingredient:
            for key, value in vars(new_meal_ingredient).items():
                if key != 'id' and value is not None:
                    setattr(meal_ingredient, key, value)
            db.session.commit()
        return meal_ingredient

    @staticmethod
    def patch(meal_ingredient_id, updates):
        meal_ingredient = MealIngredients.query.get(meal_ingredient_id)
        if meal_ingredient:
            for key, value in updates.items():
                setattr(meal_ingredient, key, value)
            db.session.commit()
        return meal_ingredient

    @staticmethod
    def put(meal_ingredient_id, new_data):
        meal_ingredient = MealIngredients.query.get(meal_ingredient_id)
        if meal_ingredient:
            for key in vars(meal_ingredient):
                if key != 'id':
                    setattr(meal_ingredient, key, new_data.get(key, None))
            db.session.commit()
        return meal_ingredient

    @staticmethod
    def delete(meal_ingredient_id):
        meal_ingredient = MealIngredients.query.get(meal_ingredient_id)
        if meal_ingredient:
            db.session.delete(meal_ingredient)
            db.session.commit()
            return True
        return False

    @staticmethod
    def delete_all():
        MealIngredients.query.delete()
        db.session.commit()
