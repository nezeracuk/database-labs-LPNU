from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response, abort
from ..controller import schedule_meal_controller
from ..domain.schedule_meal import ScheduleMeal
from ..domain.insert_record import insert_record

schedule_meal_bp = Blueprint('schedule_meal', __name__, url_prefix='/schedule_meal')

@schedule_meal_bp.route('', methods=['GET'])
def get_all_schedule_meals() -> Response:
    schedule_meals = schedule_meal_controller.find_all()
    return make_response(jsonify(schedule_meals), HTTPStatus.OK)

@schedule_meal_bp.route('', methods=['POST'])
def create_schedule_meal() -> Response:
    content = request.get_json()
    schedule_meal = ScheduleMeal.create_from_dto(content)
    schedule_meal_controller.create(schedule_meal)
    return make_response(jsonify(schedule_meal.put_into_dto()), HTTPStatus.CREATED)

@schedule_meal_bp.route('/<int:schedule_meal_id>', methods=['GET'])
def get_schedule_meal(schedule_meal_id: int) -> Response:
    schedule_meal = schedule_meal_controller.find_by_id(schedule_meal_id)
    if not schedule_meal:
        abort(HTTPStatus.NOT_FOUND, description="Schedule Meal not found")
    return make_response(jsonify(schedule_meal), HTTPStatus.OK)

@schedule_meal_bp.route('/<int:schedule_meal_id>', methods=['PUT'])
def update_schedule_meal(schedule_meal_id: int) -> Response:
    content = request.get_json()
    schedule_meal = ScheduleMeal.create_from_dto(content)
    schedule_meal_controller.update(schedule_meal_id, schedule_meal)
    return make_response("Schedule Meal updated", HTTPStatus.OK)

@schedule_meal_bp.route('/<int:schedule_meal_id>', methods=['PATCH'])
def patch_schedule_meal(schedule_meal_id: int) -> Response:
    content = request.get_json()
    schedule_meal_controller.patch(schedule_meal_id, content)
    return make_response("Schedule Meal updated", HTTPStatus.OK)

@schedule_meal_bp.route('/<int:schedule_meal_id>', methods=['DELETE'])
def delete_schedule_meal(schedule_meal_id: int) -> Response:
    schedule_meal_controller.delete(schedule_meal_id)
    return make_response("Schedule Meal deleted", HTTPStatus.OK)


@schedule_meal_bp.route('/parametrized', methods=['POST'])
def insert_schedule_meal_record():
    return insert_record(ScheduleMeal, request.get_json())