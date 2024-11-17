from .athlete_controller import AthleteController
from .schedule_meal_controller import ScheduleMealController
from .meal_controller import MealController
from .ingredient_controller import IngredientController
from .trainer_doctor_controller import TrainerDoctorController
from .competition_controller import CompetitionController
from .schedule_controller import ScheduleController
from .schedule_supplements_controller import ScheduleSupplementsController
from .supplement_controller import SupplementController
from .meal_ingredients_controller import MealIngredientsController
from .athlete_trainer_controller import AthleteTrainerController

athlete_controller = AthleteController()
schedule_meal_controller = ScheduleMealController()
meal_controller = MealController()
ingredient_controller = IngredientController()
trainer_doctor_controller = TrainerDoctorController()
competition_controller = CompetitionController()
schedule_controller = ScheduleController()
schedule_supplements_controller = ScheduleSupplementsController()
supplement_controller = SupplementController()
meal_ingredients_controller = MealIngredientsController()
athlete_trainer_controller = AthleteTrainerController()

__all__ = [
    'AthleteController',
    'ScheduleMealController',
    'MealController',
    'IngredientController',
    'TrainerDoctorController',
    'CompetitionController',
    'ScheduleController',
    'ScheduleSupplementsController',
    'SupplementController',
    'MealIngredientsController',
    'athlete_trainer_controller'
]
