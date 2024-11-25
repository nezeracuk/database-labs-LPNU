from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response, abort
from ..controller import schedule_controller
from ..domain.schedule import Schedule
from ..domain.insert_record import insert_record

schedule_bp = Blueprint('schedule', __name__, url_prefix='/schedule')

@schedule_bp.route('', methods=['GET'])
def get_all_schedules() -> Response:
    schedules = schedule_controller.find_all()
    return make_response(jsonify(schedules), HTTPStatus.OK)

@schedule_bp.route('', methods=['POST'])
def create_schedule() -> Response:
    content = request.get_json()
    schedule = Schedule.create_from_dto(content)
    schedule_controller.create(schedule)
    return make_response(jsonify(schedule.put_into_dto()), HTTPStatus.CREATED)

@schedule_bp.route('/<int:schedule_id>', methods=['GET'])
def get_schedule(schedule_id: int) -> Response:
    schedule = schedule_controller.find_by_id(schedule_id)
    if not schedule:
        abort(HTTPStatus.NOT_FOUND, description="Schedule not found")
    return make_response(jsonify(schedule), HTTPStatus.OK)

@schedule_bp.route('/<int:schedule_id>', methods=['PUT'])
def update_schedule(schedule_id: int) -> Response:
    content = request.get_json()
    schedule = Schedule.create_from_dto(content)
    schedule_controller.update(schedule_id, schedule)
    return make_response("Schedule updated", HTTPStatus.OK)

@schedule_bp.route('/<int:schedule_id>', methods=['PATCH'])
def patch_schedule(schedule_id: int) -> Response:
    content = request.get_json()
    schedule_controller.patch(schedule_id, content)
    return make_response("Schedule updated", HTTPStatus.OK)

@schedule_bp.route('/<int:schedule_id>', methods=['DELETE'])
def delete_schedule(schedule_id: int) -> Response:
    schedule_controller.delete(schedule_id)
    return make_response("Schedule deleted", HTTPStatus.OK)

@schedule_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return insert_record(Schedule, request.get_json())
