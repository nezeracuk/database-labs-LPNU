from .athlete_dao import AthleteDAO
from .schedule_meal_dao import ScheduleMealDAO
from .meal_dao import MealDAO
from .ingredient_dao import IngredientDAO
from .trainer_doctor_dao import TrainerDoctorDAO
from .competition_dao import CompetitionDAO
from .schedule_supplements_dao import ScheduleSupplementsDAO
from .schedule_dao import ScheduleDAO
from .supplement_dao import SupplementDAO
from .meal_ingredients_dao import MealIngredientsDAO
from .athlete_trainer_dao import AthleteTrainerDAO
from .athlete_statistics_dao import AthleteStatisticsDAO

athlete_dao = AthleteDAO()
schedule_meal_dao = ScheduleMealDAO()
meal_dao = MealDAO()
ingredient_dao = IngredientDAO()
trainer_doctor_dao = TrainerDoctorDAO()
competition_dao = CompetitionDAO()
schedule_supplements_dao = ScheduleSupplementsDAO()
schedule_dao = ScheduleDAO()
supplement_dao = SupplementDAO()
meal_ingredients_dao = MealIngredientsDAO()
athlete_trainer_dao = AthleteTrainerDAO()
athlete_statistics_dao = AthleteStatisticsDAO()

__all__ = [
    'athlete_dao',
    'schedule_meal_dao',
    'meal_dao',
    'ingredient_dao',
    'trainer_doctor_dao',
    'competition_dao',
    'schedule_supplements_dao',
    'schedule_dao',
    'supplement_dao',
    'meal_ingredients_dao',
    'athlete_trainer_dao',
    'athlete_statistics_dao'
]
