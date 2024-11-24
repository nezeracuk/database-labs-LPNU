from app.service.athlete_statistics_service import AthleteStatisticsService
from app.domain.athlete_statistics import AthleteStatistics
from app.controller.general_controller import GeneralController
from app import db

class AthleteStatisticsController(GeneralController):
    _service = AthleteStatisticsService()

    def create(self, data):
        # Створюємо екземпляр моделі AthleteStatistics
        new_statistic = AthleteStatistics(
            athlete_id=data.get('athlete_id'),
            total_competitions=data.get('total_competitions'),
            best_score=data.get('best_score'),
            average_score=data.get('average_score')
        )

        # Додаємо екземпляр до сесії та комітимо
        db.session.add(new_statistic)
        db.session.commit()
