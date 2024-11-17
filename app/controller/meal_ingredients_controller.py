from .general_controller import GeneralController
from ..service import meal_ingredients_service

class MealIngredientsController(GeneralController):
    _service = meal_ingredients_service
