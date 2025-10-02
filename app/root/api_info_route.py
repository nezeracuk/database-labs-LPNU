from flask import Blueprint, jsonify, Response, make_response
from http import HTTPStatus

api_info_bp = Blueprint('api_info', __name__, url_prefix='/')

@api_info_bp.route('/', methods=['GET'])
def home():
    """
    Головна сторінка API
    ---
    tags:
      - Info
    responses:
      200:
        description: Інформація про API
        schema:
          type: object
          properties:
            message:
              type: string
            api_docs:
              type: string
            endpoints:
              type: object
    """
    return make_response(jsonify({
        'message': 'Athlete Training Management System API',
        'version': '1.0.0',
        'api_docs': '/api/docs',
        'endpoints': {
            'Athletes': '/athlete',
            'Statistics': '/statistics',
            'Competitions': '/competition',
            'Trainers': '/trainer_doctor',
            'Schedules': '/schedule',
            'Meals': '/meal',
            'Schedule Meals': '/schedule_meal',
            'Ingredients': '/ingredient',
            'Supplements': '/supplement',
            'Schedule Supplements': '/schedule_supplements',
            'Meal Ingredients': '/meal_ingredients',
            'Athlete Trainers': '/athlete_trainer'
        }
    }), HTTPStatus.OK)

@api_info_bp.route('/health', methods=['GET'])
def health_check():
    """
    Перевірка стану API
    ---
    tags:
      - Info
    responses:
      200:
        description: API працює нормально
    """
    return make_response(jsonify({'status': 'healthy'}), HTTPStatus.OK)

