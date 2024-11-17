from .general_service import GeneralService
from ..dao import competition_dao

class CompetitionService(GeneralService):
    _dao = competition_dao

    def find_by_athlete_id(self, athlete_id: int):
        return self._dao.find_by_athlete_id(athlete_id)
