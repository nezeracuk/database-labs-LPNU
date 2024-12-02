from flask import Flask
from .error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)
    from .athlete_route import athlete_bp
    from .schedule_meal_route import schedule_meal_bp
    from .meal_route import meal_bp
    from .ingredient_route import ingredient_bp
    from .trainer_doctor_route import trainer_doctor_bp
    from .competition_route import competition_bp
    from .schedule_route import schedule_bp
    from .schedule_supplements_route import schedule_supplements_bp
    from .supplement_route import supplement_bp
    from .meal_ingredients_route import meal_ingredients_bp
    from .athlete_trainer_route import athlete_trainer_bp
    from .athlete_statistics_route import statistics_bp

    app.register_blueprint(athlete_bp)
    app.register_blueprint(schedule_meal_bp)
    app.register_blueprint(meal_bp)
    app.register_blueprint(ingredient_bp)
    app.register_blueprint(trainer_doctor_bp)
    app.register_blueprint(competition_bp)
    app.register_blueprint(schedule_bp)
    app.register_blueprint(schedule_supplements_bp)
    app.register_blueprint(supplement_bp)
    app.register_blueprint(meal_ingredients_bp)
    app.register_blueprint(athlete_trainer_bp)
    app.register_blueprint(statistics_bp)
