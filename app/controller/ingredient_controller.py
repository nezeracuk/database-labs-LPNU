from .general_controller import GeneralController
from ..service import ingredient_service, meal_ingredients_service

class IngredientController(GeneralController):
    _service = ingredient_service

    def get_meals_using_ingredient(self, ingredient_id: int):
        return [meal.put_into_dto() for meal in meal_ingredients_service.find_meals_by_ingredient_id(ingredient_id)]
