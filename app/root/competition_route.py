from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response, abort
from ..controller import competition_controller, athlete_controller
from ..domain.competition import Competition

competition_bp = Blueprint('competition', __name__, url_prefix='/competition')

@competition_bp.route('', methods=['GET'])
def get_all_competitions() -> Response:
    competitions = competition_controller.find_all()
    competition_dtos = [
        competition if hasattr(competition, 'put_into_dto') else competition
        for competition in competitions
    ]
    return make_response(jsonify(competition_dtos), HTTPStatus.OK)

@competition_bp.route('', methods=['POST'])
def create_competition() -> Response:
    content = request.get_json()
    competition = Competition.create_from_dto(content)
    competition_controller.create(competition)
    return make_response(jsonify(competition.put_into_dto()), HTTPStatus.CREATED)

@competition_bp.route('/<int:competition_id>', methods=['GET'])
def get_competition(competition_id: int) -> Response:
    competition = competition_controller.find_by_id(competition_id)
    if not competition:
        abort(HTTPStatus.NOT_FOUND, description="Competition not found")
    return make_response(jsonify(competition), HTTPStatus.OK)

@competition_bp.route('/<int:competition_id>', methods=['PUT'])
def update_competition(competition_id: int) -> Response:
    content = request.get_json()
    competition = Competition.create_from_dto(content)
    competition_controller.update(competition_id, competition)
    return make_response("Competition updated", HTTPStatus.OK)

@competition_bp.route('/<int:competition_id>', methods=['PATCH'])
def patch_competition(competition_id: int) -> Response:
    content = request.get_json()
    competition_controller.patch(competition_id, content)
    return make_response("Competition updated", HTTPStatus.OK)

@competition_bp.route('/<int:competition_id>', methods=['DELETE'])
def delete_competition(competition_id: int) -> Response:
    competition_controller.delete(competition_id)
    return make_response("Competition deleted", HTTPStatus.OK)
