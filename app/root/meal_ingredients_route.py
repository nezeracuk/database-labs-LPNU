from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response, abort
from ..controller import meal_ingredients_controller
from ..domain.meal_ingredients import MealIngredients

meal_ingredients_bp = Blueprint('meal_ingredients', __name__, url_prefix='/meal_ingredients')

@meal_ingredients_bp.route('', methods=['GET'])
def get_all_meal_ingredients() -> Response:
    meal_ingredients = meal_ingredients_controller.find_all()
    return make_response(jsonify(meal_ingredients), HTTPStatus.OK)

@meal_ingredients_bp.route('', methods=['POST'])
def create_meal_ingredient() -> Response:
    content = request.get_json()
    meal_ingredient = MealIngredients.create_from_dto(content)
    meal_ingredients_controller.create(meal_ingredient)
    return make_response(jsonify(meal_ingredient.put_into_dto()), HTTPStatus.CREATED)

@meal_ingredients_bp.route('/<int:meal_ingredient_id>', methods=['GET'])
def get_meal_ingredient(meal_ingredient_id: int) -> Response:
    meal_ingredient = meal_ingredients_controller.find_by_id(meal_ingredient_id)
    if not meal_ingredient:
        abort(HTTPStatus.NOT_FOUND, description="Meal Ingredient not found")
    return make_response(jsonify(meal_ingredient), HTTPStatus.OK)

@meal_ingredients_bp.route('/<int:meal_ingredient_id>', methods=['PUT'])
def update_meal_ingredient(meal_ingredient_id: int) -> Response:
    content = request.get_json()
    meal_ingredient = MealIngredients.create_from_dto(content)
    meal_ingredients_controller.update(meal_ingredient_id, meal_ingredient)
    return make_response("Meal Ingredient updated", HTTPStatus.OK)

@meal_ingredients_bp.route('/<int:meal_ingredient_id>', methods=['PATCH'])
def patch_meal_ingredient(meal_ingredient_id: int) -> Response:
    content = request.get_json()
    meal_ingredients_controller.patch(meal_ingredient_id, content)
    return make_response("Meal Ingredient updated", HTTPStatus.OK)

@meal_ingredients_bp.route('/<int:meal_ingredient_id>', methods=['DELETE'])
def delete_meal_ingredient(meal_ingredient_id: int) -> Response:
    meal_ingredients_controller.delete(meal_ingredient_id)
    return make_response("Meal Ingredient deleted", HTTPStatus.OK)
