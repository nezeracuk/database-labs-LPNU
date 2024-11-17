from .. import db
from ..domain.schedule import Schedule

class ScheduleDAO:
    @staticmethod
    def find_all():
        return Schedule.query.all()

    @staticmethod
    def find_by_id(schedule_id):
        schedule = Schedule.query.get(schedule_id)
        if schedule:
            db.session.refresh(schedule)
        return schedule

    @staticmethod
    def find_by_athlete_id(athlete_id):
        return Schedule.query.filter_by(athlete_id=athlete_id).all()

    @staticmethod
    def create(schedule):
        db.session.add(schedule)
        db.session.commit()
        return schedule

    @staticmethod
    def update(schedule_id, new_schedule):
        schedule = Schedule.query.get(schedule_id)
        if schedule:
            for key, value in vars(new_schedule).items():
                if key != 'id' and value is not None:
                    setattr(schedule, key, value)
            db.session.commit()
        return schedule

    @staticmethod
    def patch(schedule_id, updates):
        schedule = Schedule.query.get(schedule_id)
        if schedule:
            for key, value in updates.items():
                setattr(schedule, key, value)
            db.session.commit()
        return schedule

    @staticmethod
    def put(schedule_id, new_data):
        schedule = Schedule.query.get(schedule_id)
        if schedule:
            for key in vars(schedule):
                if key != 'id':
                    setattr(schedule, key, new_data.get(key, None))
            db.session.commit()
        return schedule

    @staticmethod
    def delete(schedule_id):
        schedule = Schedule.query.get(schedule_id)
        if schedule:
            db.session.delete(schedule)
            db.session.commit()
            return True
        return False

    @staticmethod
    def delete_all():
        Schedule.query.delete()
        db.session.commit()
