from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import athlete_controller, competition_controller
from ..domain.athlete import Athlete
from ..domain.insert_record import insert_record

athlete_bp = Blueprint('athlete', __name__, url_prefix='/athlete')

@athlete_bp.route('', methods=['GET'])
def get_all_athletes() -> Response:
    """
    Get all athletes
    ---
    tags:
      - Athletes
    responses:
      200:
        description: List of all athletes
    """
    athletes = athlete_controller.find_all()
    for athlete in athletes:
        athlete['competitions'] = competition_controller.find_by_athlete_id(athlete['id'])
    return make_response(jsonify(athletes), HTTPStatus.OK)

@athlete_bp.route('', methods=['POST'])
def create_athlete() -> Response:
    """
    Create a new athlete
    ---
    tags:
      - Athletes
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - firstname
            - lastname
          properties:
            firstname:
              type: string
            lastname:
              type: string
            height:
              type: number
            weight:
              type: number
    responses:
      201:
        description: Athlete created successfully
    """
    content = request.get_json()
    athlete = Athlete.create_from_dto(content)
    athlete_controller.create(athlete)
    return make_response(jsonify(athlete.put_into_dto()), HTTPStatus.CREATED)

@athlete_bp.route('/<int:athlete_id>', methods=['GET'])
def get_athlete(athlete_id: int) -> Response:
    """
    Get athlete by ID
    ---
    tags:
      - Athletes
    parameters:
      - name: athlete_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Athlete details
    """
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
    """
    Delete athlete
    ---
    tags:
      - Athletes
    parameters:
      - name: athlete_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Athlete deleted successfully
    """
    athlete_controller.delete(athlete_id)
    return make_response("Athlete deleted", HTTPStatus.OK)

@athlete_bp.route('/parametrized', methods=['POST'])
def insert_athlete_record():
    return insert_record(Athlete, request.get_json())
