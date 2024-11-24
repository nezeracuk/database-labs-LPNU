from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import athlete_trainer_controller
from ..domain.athlete_trainer import AthleteTrainer
from ..domain.trainer_doctor import TrainerDoctor

athlete_trainer_bp = Blueprint('athlete_trainer', __name__, url_prefix='/athlete-trainer')

@athlete_trainer_bp.route('', methods=['GET'])
def get_all_relations() -> Response:
    """
    Отримати всі зв'язки атлетів і тренерів.
    """
    relations = athlete_trainer_controller.find_all()
    return make_response(jsonify(relations), HTTPStatus.OK)

@athlete_trainer_bp.route('', methods=['POST'])
def create_relation() -> Response:
    """
    Створити новий зв'язок між атлетом і тренером.
    """
    content = request.get_json()
    relation = AthleteTrainer.create_from_dto(content)
    athlete_trainer_controller.create(relation)
    return make_response(jsonify(relation.put_into_dto()), HTTPStatus.CREATED)

@athlete_trainer_bp.route('/<int:athlete_id>/<int:trainer_doctor_id>', methods=['GET'])
def get_relation(athlete_id: int, trainer_doctor_id: int) -> Response:
    """
    Отримати конкретний зв'язок між атлетом і тренером.
    """
    relation = athlete_trainer_controller.find_by_id(athlete_id, trainer_doctor_id)
    if relation:
        return make_response(jsonify(relation), HTTPStatus.OK)
    return make_response("Relation not found", HTTPStatus.NOT_FOUND)

@athlete_trainer_bp.route('/<int:athlete_id>/<int:trainer_doctor_id>', methods=['PUT'])
def update_relation(athlete_id: int, trainer_doctor_id: int) -> Response:
    content = request.get_json()
    if not content:
        return make_response("Invalid data", HTTPStatus.BAD_REQUEST)

    updated_relation = athlete_trainer_controller.put(athlete_id, trainer_doctor_id, content)
    if updated_relation:
        return make_response(jsonify(updated_relation.put_into_dto()), HTTPStatus.OK)
    return make_response("Relation not found", HTTPStatus.NOT_FOUND)

@athlete_trainer_bp.route('/<int:athlete_id>/<int:trainer_doctor_id>', methods=['PATCH'])
def patch_relation(athlete_id: int, trainer_doctor_id: int) -> Response:
    content = request.get_json()
    if not content:
        return make_response("Invalid data", HTTPStatus.BAD_REQUEST)

    patched_relation = athlete_trainer_controller.patch(athlete_id, trainer_doctor_id, content)
    if patched_relation:
        return make_response(jsonify(patched_relation.put_into_dto()), HTTPStatus.OK)
    return make_response("Relation not found", HTTPStatus.NOT_FOUND)

@athlete_trainer_bp.route('/<int:athlete_id>/<int:trainer_doctor_id>', methods=['DELETE'])
def delete_relation(athlete_id: int, trainer_doctor_id: int) -> Response:
    """
    Видалити зв'язок між атлетом і тренером.
    """
    athlete_trainer_controller.delete(athlete_id, trainer_doctor_id)
    return make_response("Relation deleted", HTTPStatus.OK)


@athlete_trainer_bp.route('/new_link', methods=['POST'])
def add_athlete_trainer():
    data = request.get_json()
    athlete_name = data['athlete']
    trainer_doctor_name = data['trainer_doctor']

    try:
        new_link = AthleteTrainer.add_athlete_trainer(athlete_name, trainer_doctor_name)
        return make_response(jsonify(new_link.put_into_dto()), HTTPStatus.CREATED)
    except ValueError as e:
        return make_response(str(e), HTTPStatus.BAD_REQUEST)
