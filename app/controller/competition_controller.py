from .general_controller import GeneralController
from ..service import competition_service

class CompetitionController(GeneralController):
    _service = competition_service

    def find_by_athlete_id(self, athlete_id: int):
        return [competition.put_into_dto() for competition in self._service.find_by_athlete_id(athlete_id)]
