from app.dao.athlete_statistics_dao import AthleteStatisticsDAO
from app.service.general_service import GeneralService

class AthleteStatisticsService(GeneralService):
    _dao = AthleteStatisticsDAO()

    def create_statistics(self, athlete_id, data):
        statistics = {
            "athlete_id": athlete_id,
            "total_competitions": data["total_competitions"],
            "best_score": data["best_score"],
            "average_score": data["average_score"]
        }
        self.dao.insert_statistics(statistics)
