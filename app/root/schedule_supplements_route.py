from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response, abort
from ..controller import schedule_supplements_controller
from ..domain.schedule_supplements import ScheduleSupplements
from ..domain.insert_record import insert_record

schedule_supplements_bp = Blueprint('schedule_supplements', __name__, url_prefix='/schedule_supplements')

@schedule_supplements_bp.route('', methods=['GET'])
def get_all_schedule_supplements() -> Response:
    schedule_supplements = schedule_supplements_controller.find_all()
    return make_response(jsonify(schedule_supplements), HTTPStatus.OK)

@schedule_supplements_bp.route('', methods=['POST'])
def create_schedule_supplement() -> Response:
    content = request.get_json()
    schedule_supplement = ScheduleSupplements.create_from_dto(content)
    schedule_supplements_controller.create(schedule_supplement)
    return make_response(jsonify(schedule_supplement.put_into_dto()), HTTPStatus.CREATED)

@schedule_supplements_bp.route('/<int:schedule_supplements_id>', methods=['GET'])
def get_schedule_supplement(schedule_supplements_id: int) -> Response:
    schedule_supplement = schedule_supplements_controller.find_by_id(schedule_supplements_id)
    if not schedule_supplement:
        abort(HTTPStatus.NOT_FOUND, description="Schedule Supplement not found")
    return make_response(jsonify(schedule_supplement), HTTPStatus.OK)

@schedule_supplements_bp.route('/<int:schedule_supplements_id>', methods=['PUT'])
def update_schedule_supplement(schedule_supplements_id: int) -> Response:
    content = request.get_json()
    schedule_supplement = ScheduleSupplements.create_from_dto(content)
    schedule_supplements_controller.update(schedule_supplements_id, schedule_supplement)
    return make_response("Schedule Supplements updated", HTTPStatus.OK)

@schedule_supplements_bp.route('/<int:schedule_supplements_id>', methods=['PATCH'])
def patch_schedule_supplement(schedule_supplements_id: int) -> Response:
    content = request.get_json()
    schedule_supplements_controller.patch(schedule_supplements_id, content)
    return make_response("Schedule Supplements updated", HTTPStatus.OK)

@schedule_supplements_bp.route('/<int:schedule_supplements_id>', methods=['DELETE'])
def delete_schedule_supplement(schedule_supplements_id: int) -> Response:
    schedule_supplements_controller.delete(schedule_supplements_id)
    return make_response("Schedule Supplements deleted", HTTPStatus.OK)

@schedule_supplements_bp.route('/parametrized', methods=['POST'])
def insert_schedule_supplements_record():
    return insert_record(ScheduleSupplements, request.get_json())
