from .general_controller import GeneralController
from ..service import meal_service, meal_ingredients_service

class MealController(GeneralController):
    _service = meal_service

    def get_ingredients_for_meal(self, meal_id: int):
        return [ingredient.put_into_dto() for ingredient in meal_ingredients_service.find_by_meal_id(meal_id)]
