from app import db
from ..domain.athlete_statistics import AthleteStatistics

class AthleteStatisticsDAO:
    @staticmethod
    def find_all():
        return AthleteStatistics.query.all()

    @staticmethod
    def find_by_id(athlete_id):
        return AthleteStatistics.query.filter_by(athlete_id=athlete_id).first()

    @staticmethod
    def create(statistics):
        db.session.add(statistics)
        db.session.commit()
        return statistics

    @staticmethod
    def update(athlete_id, updates):
        statistics = AthleteStatisticsDAO.find_by_id(athlete_id)
        if statistics:
            for key, value in updates.items():
                setattr(statistics, key, value)
            db.session.commit()
            return statistics
        return None

    @staticmethod
    def delete(athlete_id):
        statistics = AthleteStatisticsDAO.find_by_id(athlete_id)
        if statistics:
            db.session.delete(statistics)
            db.session.commit()
