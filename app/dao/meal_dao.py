from .. import db
from ..domain.meal import Meal

class MealDAO:
    @staticmethod
    def find_all():
        return Meal.query.all()

    @staticmethod
    def find_by_id(meal_id):
        meal = Meal.query.get(meal_id)
        if meal:
            db.session.refresh(meal)
        return meal

    @staticmethod
    def create(meal):
        db.session.add(meal)
        db.session.commit()
        return meal

    @staticmethod
    def create_all(meals):
        db.session.bulk_save_objects(meals)
        db.session.commit()
        return meals

    @staticmethod
    def update(meal_id, new_meal):
        meal = Meal.query.get(meal_id)
        if meal:
            for key, value in vars(new_meal).items():
                if key != 'id' and value is not None:
                    setattr(meal, key, value)
            db.session.commit()
        return meal

    @staticmethod
    def patch(meal_id, updates):
        meal = Meal.query.get(meal_id)
        if meal:
            for key, value in updates.items():
                setattr(meal, key, value)
            db.session.commit()
        return meal

    @staticmethod
    def put(meal_id, new_data):
        meal = Meal.query.get(meal_id)
        if meal:
            for key in vars(meal):
                if key != 'id':
                    setattr(meal, key, new_data.get(key, None))
            db.session.commit()
        return meal

    @staticmethod
    def delete(meal_id):
        meal = Meal.query.get(meal_id)
        if meal:
            db.session.delete(meal)
            db.session.commit()
            return True
        return False

    @staticmethod
    def delete_all():
        Meal.query.delete()
        db.session.commit()
