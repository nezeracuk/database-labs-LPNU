from .. import db
from ..domain.competition import Competition

class CompetitionDAO:
    @staticmethod
    def find_all():
        return Competition.query.all()

    @staticmethod
    def find_by_id(competition_id):
        competition = Competition.query.get(competition_id)
        if competition:
            db.session.refresh(competition)
        return competition

    @staticmethod
    def find_by_athlete_id(athlete_id):
        return Competition.query.filter_by(athlete_id=athlete_id).all()

    @staticmethod
    def create(competition):
        db.session.add(competition)
        db.session.commit()
        return competition

    @staticmethod
    def update(competition_id, new_competition):
        competition = Competition.query.get(competition_id)
        if competition:
            for key, value in vars(new_competition).items():
                if key != 'id' and value is not None:
                    setattr(competition, key, value)
            db.session.commit()
        return competition

    @staticmethod
    def patch(competition_id, updates):
        competition = Competition.query.get(competition_id)
        if competition:
            for key, value in updates.items():
                setattr(competition, key, value)
            db.session.commit()
        return competition

    @staticmethod
    def put(competition_id, new_data):
        competition = Competition.query.get(competition_id)
        if competition:
            for key in vars(competition):
                if key != 'id':
                    setattr(competition, key, new_data.get(key, None))
            db.session.commit()
        return competition

    @staticmethod
    def delete(competition_id):
        competition = Competition.query.get(competition_id)
        if competition:
            db.session.delete(competition)
            db.session.commit()
            return True
        return False

    @staticmethod
    def delete_all():
        Competition.query.delete()
        db.session.commit()
