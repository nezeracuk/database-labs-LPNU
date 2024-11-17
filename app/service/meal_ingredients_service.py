from .general_service import GeneralService
from ..dao import meal_ingredients_dao


class MealIngredientsService(GeneralService):
    _dao = meal_ingredients_dao
