from .general_service import GeneralService
from ..dao import schedule_meal_dao


class ScheduleMealService(GeneralService):
    _dao = schedule_meal_dao
