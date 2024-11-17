from .general_controller import GeneralController
from ..service import athlete_trainer_service

class AthleteTrainerController(GeneralController):
    _service = athlete_trainer_service

    def patch(self, athlete_id: int, trainer_doctor_id: int, updates: dict):
        """
        Часткове оновлення зв'язку між атлетом і тренером.
        """
        return self._service.patch(athlete_id, trainer_doctor_id, updates)

