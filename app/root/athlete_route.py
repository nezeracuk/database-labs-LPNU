from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import athlete_controller, competition_controller
from ..domain.athlete import Athlete

athlete_bp = Blueprint('athlete', __name__, url_prefix='/athlete')

@athlete_bp.route('', methods=['GET'])
def get_all_athletes() -> Response:
    athletes = athlete_controller.find_all()
    for athlete in athletes:
        athlete['competitions'] = competition_controller.find_by_athlete_id(athlete['id'])
    return make_response(jsonify(athletes), HTTPStatus.OK)

@athlete_bp.route('', methods=['POST'])
def create_athlete() -> Response:
    content = request.get_json()
    athlete = Athlete.create_from_dto(content)
    athlete_controller.create(athlete)
    return make_response(jsonify(athlete.put_into_dto()), HTTPStatus.CREATED)

@athlete_bp.route('/<int:athlete_id>', methods=['GET'])
def get_athlete(athlete_id: int) -> Response:
    return make_response(jsonify(athlete_controller.find_by_id(athlete_id)), HTTPStatus.OK)

@athlete_bp.route('/<int:athlete_id>', methods=['PUT'])
def update_athlete(athlete_id: int) -> Response:
    content = request.get_json()
    athlete = Athlete.create_from_dto(content)
    athlete_controller.update(athlete_id, athlete)
    return make_response("Athlete updated", HTTPStatus.OK)

@athlete_bp.route('/<int:athlete_id>', methods=['PATCH'])
def patch_athlete(athlete_id: int) -> Response:
    content = request.get_json()
    athlete_controller.patch(athlete_id, content)
    return make_response("Athlete updated", HTTPStatus.OK)

@athlete_bp.route('/<int:athlete_id>', methods=['DELETE'])
def delete_athlete(athlete_id: int) -> Response:
    athlete_controller.delete(athlete_id)
    return make_response("Athlete deleted", HTTPStatus.OK)
