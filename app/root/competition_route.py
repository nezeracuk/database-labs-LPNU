from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response, abort
from ..controller import competition_controller, athlete_controller
from ..domain.competition import Competition
from ..domain.insert_record import insert_record

competition_bp = Blueprint('competition', __name__, url_prefix='/competition')

@competition_bp.route('', methods=['GET'])
def get_all_competitions() -> Response:
    """
    Get all competitions
    ---
    tags:
      - Competitions
    responses:
      200:
        description: List of all competitions
    """
    competitions = competition_controller.find_all()
    competition_dtos = [
        competition if hasattr(competition, 'put_into_dto') else competition
        for competition in competitions
    ]
    return make_response(jsonify(competition_dtos), HTTPStatus.OK)

@competition_bp.route('', methods=['POST'])
def create_competition() -> Response:
    """
    Create a new competition
    ---
    tags:
      - Competitions
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - name
            - date
            - Location
            - athlete_id
          properties:
            name:
              type: string
            date:
              type: string
              format: date
            Location:
              type: string
            athlete_id:
              type: integer
    responses:
      201:
        description: Competition created successfully
    """
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
    """
    Delete competition
    ---
    tags:
      - Competitions
    parameters:
      - name: competition_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Competition deleted successfully
    """
    competition_controller.delete(competition_id)
    return make_response("Competition deleted", HTTPStatus.OK)


@competition_bp.route('/parametrized', methods=['POST'])
def insert_competition_record():
    return insert_record(Competition, request.get_json())
