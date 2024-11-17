from .general_service import GeneralService
from ..dao import meal_dao


class MealService(GeneralService):
    _dao = meal_dao
