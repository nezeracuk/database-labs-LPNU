from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response, abort
from ..controller import supplement_controller
from ..domain.supplement import Supplement

supplement_bp = Blueprint('supplement', __name__, url_prefix='/supplement')

@supplement_bp.route('', methods=['GET'])
def get_all_supplements() -> Response:
    supplements = supplement_controller.find_all()
    return make_response(jsonify(supplements), HTTPStatus.OK)

@supplement_bp.route('', methods=['POST'])
def create_supplement() -> Response:
    content = request.get_json()
    supplement = Supplement.create_from_dto(content)
    supplement_controller.create(supplement)
    return make_response(jsonify(supplement.put_into_dto()), HTTPStatus.CREATED)

@supplement_bp.route('/<int:supplement_id>', methods=['GET'])
def get_supplement(supplement_id: int) -> Response:
    supplement = supplement_controller.find_by_id(supplement_id)
    if not supplement:
        abort(HTTPStatus.NOT_FOUND, description="Supplement not found")
    return make_response(jsonify(supplement), HTTPStatus.OK)

@supplement_bp.route('/<int:supplement_id>', methods=['PUT'])
def update_supplement(supplement_id: int) -> Response:
    content = request.get_json()
    supplement = Supplement.create_from_dto(content)
    supplement_controller.update(supplement_id, supplement)
    return make_response("Supplement updated", HTTPStatus.OK)

@supplement_bp.route('/<int:supplement_id>', methods=['PATCH'])
def patch_supplement(supplement_id: int) -> Response:
    content = request.get_json()
    supplement_controller.patch(supplement_id, content)
    return make_response("Supplement updated", HTTPStatus.OK)

@supplement_bp.route('/<int:supplement_id>', methods=['DELETE'])
def delete_supplement(supplement_id: int) -> Response:
    supplement_controller.delete(supplement_id)
    return make_response("Supplement deleted", HTTPStatus.OK)
