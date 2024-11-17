from .general_controller import GeneralController
from ..service import athlete_service, competition_service

class AthleteController(GeneralController):
    _service = athlete_service

    def get_competitions_for_athlete(self, athlete_id: int):
        return [competition.put_into_dto() for competition in competition_service.find_by_athlete_id(athlete_id)]

    def find_all_with_competitions(self):
        athletes = self._service.find_all()
        for athlete in athletes:
            athlete.competitions = competition_service.find_by_athlete_id(athlete.id)
        return [athlete.put_into_dto() for athlete in athletes]

    def find_by_id_with_competitions(self, athlete_id: int):
        athlete = self._service.find_by_id(athlete_id)
        if athlete:
            athlete.competitions = competition_service.find_by_athlete_id(athlete.id)
        return athlete.put_into_dto() if athlete else None
