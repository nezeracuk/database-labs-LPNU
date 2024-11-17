from .. import db
from ..domain.athlete import Athlete

class AthleteDAO:
    @staticmethod
    def find_all():
        return Athlete.query.all()

    @staticmethod
    def find_by_id(athlete_id):
        return Athlete.query.get(athlete_id)

    @staticmethod
    def create(athlete):
        db.session.add(athlete)
        db.session.commit()
        return athlete

    @staticmethod
    def create_all(athletes):
        db.session.bulk_save_objects(athletes)
        db.session.commit()
        return athletes

    @staticmethod
    def update(athlete_id, new_athlete):
        athlete = Athlete.query.get(athlete_id)
        if athlete:
            for key, value in vars(new_athlete).items():
                if key != 'id' and value is not None:
                    setattr(athlete, key, value)
            db.session.commit()
        return athlete

    @staticmethod
    def patch(athlete_id, updates):
        athlete = Athlete.query.get(athlete_id)
        if athlete:
            for key, value in updates.items():
                setattr(athlete, key, value)
            db.session.commit()
        return athlete

    @staticmethod
    def put(athlete_id, new_data):
        athlete = Athlete.query.get(athlete_id)
        if athlete:
            for key in vars(athlete):
                if key != 'id':
                    setattr(athlete, key, new_data.get(key, None))
            db.session.commit()
        return athlete

    @staticmethod
    def delete(athlete_id):
        athlete = Athlete.query.get(athlete_id)
        if athlete:
            db.session.delete(athlete)
            db.session.commit()
            return True
        return False

    @staticmethod
    def delete_all():
        Athlete.query.delete()
        db.session.commit()
