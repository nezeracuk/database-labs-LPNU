from .general_controller import GeneralController
from ..service import schedule_meal_service, meal_service

class ScheduleMealController(GeneralController):
    _service = schedule_meal_service

    def get_meals_for_schedule(self, schedule_meal_id: int):
        return [meal.put_into_dto() for meal in meal_service.find_by_schedule_meal_id(schedule_meal_id)]
