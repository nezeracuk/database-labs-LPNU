from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response, abort
from ..controller import trainer_doctor_controller
from ..domain.trainer_doctor import TrainerDoctor

trainer_doctor_bp = Blueprint('trainer_doctor', __name__, url_prefix='/trainer_doctor')

@trainer_doctor_bp.route('', methods=['GET'])
def get_all_trainers_doctors() -> Response:
    trainers_doctors = trainer_doctor_controller.find_all()
    return make_response(jsonify(trainers_doctors), HTTPStatus.OK)

@trainer_doctor_bp.route('', methods=['POST'])
def create_trainer_doctor() -> Response:
    content = request.get_json()
    trainer_doctor = TrainerDoctor.create_from_dto(content)
    trainer_doctor_controller.create(trainer_doctor)
    return make_response(jsonify(trainer_doctor.put_into_dto()), HTTPStatus.CREATED)

@trainer_doctor_bp.route('/<int:trainer_doctor_id>', methods=['GET'])
def get_trainer_doctor(trainer_doctor_id: int) -> Response:
    trainer_doctor = trainer_doctor_controller.find_by_id(trainer_doctor_id)
    if not trainer_doctor:
        abort(HTTPStatus.NOT_FOUND, description="Trainer/Doctor not found")
    return make_response(jsonify(trainer_doctor), HTTPStatus.OK)

@trainer_doctor_bp.route('/<int:trainer_doctor_id>', methods=['PUT'])
def update_trainer_doctor(trainer_doctor_id: int) -> Response:
    content = request.get_json()
    trainer_doctor = TrainerDoctor.create_from_dto(content)
    trainer_doctor_controller.update(trainer_doctor_id, trainer_doctor)
    return make_response("Trainer/Doctor updated", HTTPStatus.OK)

@trainer_doctor_bp.route('/<int:trainer_doctor_id>', methods=['PATCH'])
def patch_trainer_doctor(trainer_doctor_id: int) -> Response:
    content = request.get_json()
    trainer_doctor_controller.patch(trainer_doctor_id, content)
    return make_response("Trainer/Doctor updated", HTTPStatus.OK)

@trainer_doctor_bp.route('/<int:trainer_doctor_id>', methods=['DELETE'])
def delete_trainer_doctor(trainer_doctor_id: int) -> Response:
    trainer_doctor_controller.delete(trainer_doctor_id)
    return make_response("Trainer/Doctor deleted", HTTPStatus.OK)

@trainer_doctor_bp.route('/insert_dummy_data', methods=['POST'])
def insert_dummy_trainers():
    """
    API endpoint to insert 10 dummy rows into the TrainerDoctor table.
    """
    try:
        TrainerDoctor.insert_dummy_data()
        return make_response(jsonify({"message": "10 dummy trainers inserted successfully"}), HTTPStatus.CREATED)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)