from .. import db
from ..domain.schedule_meal import ScheduleMeal

class ScheduleMealDAO:
    @staticmethod
    def find_all():
        return ScheduleMeal.query.all()

    @staticmethod
    def find_by_id(schedule_meal_id):
        schedule_meal = ScheduleMeal.query.get(schedule_meal_id)
        if schedule_meal:
            db.session.refresh(schedule_meal)
        return schedule_meal

    @staticmethod
    def find_by_schedule_id(schedule_id):
        return ScheduleMeal.query.filter_by(schedule_id=schedule_id).all()

    @staticmethod
    def create(schedule_meal):
        db.session.add(schedule_meal)
        db.session.commit()
        return schedule_meal

    @staticmethod
    def update(schedule_meal_id, new_schedule_meal):
        schedule_meal = ScheduleMeal.query.get(schedule_meal_id)
        if schedule_meal:
            for key, value in vars(new_schedule_meal).items():
                if key != 'id' and value is not None:
                    setattr(schedule_meal, key, value)
            db.session.commit()
        return schedule_meal

    @staticmethod
    def patch(schedule_meal_id, updates):
        schedule_meal = ScheduleMeal.query.get(schedule_meal_id)
        if schedule_meal:
            for key, value in updates.items():
                setattr(schedule_meal, key, value)
            db.session.commit()
        return schedule_meal

    @staticmethod
    def put(schedule_meal_id, new_data):
        schedule_meal = ScheduleMeal.query.get(schedule_meal_id)
        if schedule_meal:
            for key in vars(schedule_meal):
                if key != 'id':
                    setattr(schedule_meal, key, new_data.get(key, None))
            db.session.commit()
        return schedule_meal

    @staticmethod
    def delete(schedule_meal_id):
        schedule_meal = ScheduleMeal.query.get(schedule_meal_id)
        if schedule_meal:
            db.session.delete(schedule_meal)
            db.session.commit()
            return True
        return False

    @staticmethod
    def delete_all():
        ScheduleMeal.query.delete()
        db.session.commit()
