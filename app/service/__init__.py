from .athlete_service import AthleteService
from .schedule_meal_service import ScheduleMealService
from .meal_service import MealService
from .ingredient_service import IngredientService
from .trainer_doctor_service import TrainerDoctorService
from .competition_service import CompetitionService
from .schedule_service import ScheduleService
from .schedule_supplements_service import ScheduleSupplementsService
from .supplement_service import SupplementService
from .meal_ingredients_service import MealIngredientsService
from .athlete_trainer_service import AthleteTrainerService

athlete_service = AthleteService()
schedule_meal_service = ScheduleMealService()
meal_service = MealService()
ingredient_service = IngredientService()
trainer_doctor_service = TrainerDoctorService()
competition_service = CompetitionService()
schedule_service = ScheduleService()
schedule_supplements_service = ScheduleSupplementsService()
supplement_service = SupplementService()
meal_ingredients_service = MealIngredientsService()
athlete_trainer_service = AthleteTrainerService()

__all__ = [
    'AthleteService',
    'ScheduleMealService',
    'MealService',
    'IngredientService',
    'TrainerDoctorService',
    'CompetitionService',
    'ScheduleService',
    'ScheduleSupplementsService',
    'SupplementService',
    'MealIngredientsService',
    'athlete_trainer_service'
]
