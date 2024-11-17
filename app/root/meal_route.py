from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response, abort
from ..controller import meal_controller
from ..domain.meal import Meal

meal_bp = Blueprint('meal', __name__, url_prefix='/meal')

@meal_bp.route('', methods=['GET'])
def get_all_meals() -> Response:
    meals = meal_controller.find_all()
    meal_dtos = [
        meal if hasattr(meal, 'put_into_dto') else meal
        for meal in meals
    ]
    return make_response(jsonify(meal_dtos), HTTPStatus.OK)

@meal_bp.route('', methods=['POST'])
def create_meal() -> Response:
    content = request.get_json()
    meal = Meal.create_from_dto(content)
    meal_controller.create(meal)
    return make_response(jsonify(meal.put_into_dto()), HTTPStatus.CREATED)

@meal_bp.route('/<int:meal_id>', methods=['GET'])
def get_meal(meal_id: int) -> Response:
    meal = meal_controller.find_by_id(meal_id)
    if not meal:
        abort(HTTPStatus.NOT_FOUND, description="Meal not found")
    return make_response(jsonify(meal), HTTPStatus.OK)

@meal_bp.route('/<int:meal_id>', methods=['PUT'])
def update_meal(meal_id: int) -> Response:
    content = request.get_json()
    meal = Meal.create_from_dto(content)
    meal_controller.update(meal_id, meal)
    return make_response("Meal updated", HTTPStatus.OK)

@meal_bp.route('/<int:meal_id>', methods=['PATCH'])
def patch_meal(meal_id: int) -> Response:
    content = request.get_json()
    meal_controller.patch(meal_id, content)
    return make_response("Meal updated", HTTPStatus.OK)

@meal_bp.route('/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id: int) -> Response:
    meal_controller.delete(meal_id)
    return make_response("Meal deleted", HTTPStatus.OK)
