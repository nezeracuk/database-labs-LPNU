from .general_controller import GeneralController
from ..service import schedule_service, athlete_service, schedule_meal_service, schedule_supplements_service

class ScheduleController(GeneralController):
    _service = schedule_service

    def get_athlete_for_schedule(self, schedule_id: int):
        athlete = athlete_service.find_by_schedule_id(schedule_id)
        return athlete.put_into_dto() if athlete else None

    def get_meal_for_schedule(self, schedule_id: int):
        schedule_meal = schedule_meal_service.find_by_schedule_id(schedule_id)
        return schedule_meal.put_into_dto() if schedule_meal else None

    def get_supplements_for_schedule(self, schedule_id: int):
        schedule_supplements = schedule_supplements_service.find_by_schedule_id(schedule_id)
        return schedule_supplements.put_into_dto() if schedule_supplements else None
