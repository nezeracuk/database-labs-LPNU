from .general_service import GeneralService
from ..dao import athlete_trainer_dao


class AthleteTrainerService(GeneralService):
    _dao = athlete_trainer_dao

    def patch(self, athlete_id: int, trainer_doctor_id: int, updates: dict):
        """
        Часткове оновлення запису через DAO.
        """
        return self._dao.patch(athlete_id, trainer_doctor_id, updates)


    def put(self, athlete_id: int, trainer_doctor_id: int, new_data: dict):
        return self._dao.put(athlete_id, trainer_doctor_id, new_data)

