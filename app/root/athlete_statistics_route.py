from flask import Blueprint, request, jsonify
from app.controller.athlete_statistics_controller import AthleteStatisticsController
from app.domain.athlete_statistics import AthleteStatistics

statistics_bp = Blueprint('statistics', __name__, url_prefix='/statistics')

# Отримати всі записи
@statistics_bp.route('', methods=['GET'])
def get_all_statistics():
    return jsonify(AthleteStatisticsController().find_all())

# Отримати конкретний запис
@statistics_bp.route('/<int:statistics_id>', methods=['GET'])
def get_statistics(statistics_id):
    return jsonify(AthleteStatisticsController().find_by_id(statistics_id))

# Створити новий запис
@statistics_bp.route('', methods=['POST'])
def create_statistics():
    data = request.json
    if not data:
        return jsonify({'error': 'Invalid data'}), 400

    try:
        AthleteStatisticsController().create(data)
        return jsonify({'message': 'Athlete statistics added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@statistics_bp.route('/<int:statistics_id>', methods=['PUT'])
def update_statistics(statistics_id):
    data = request.json
    try:
        AthleteStatisticsController().update(statistics_id, data)
        return jsonify({'message': 'Updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Видалити запис
@statistics_bp.route('/<int:statistics_id>', methods=['DELETE'])
def delete_statistics(statistics_id):
    try:
        AthleteStatisticsController().delete(statistics_id)
        return jsonify({'message': 'Deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Часткове оновлення запису
@statistics_bp.route('/<int:statistics_id>', methods=['PATCH'])
def patch_statistics(statistics_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        AthleteStatisticsController().patch(statistics_id, data)
        return jsonify({'message': 'Statistics updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
