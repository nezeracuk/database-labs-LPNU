from .. import db
from ..domain.schedule_supplements import ScheduleSupplements

class ScheduleSupplementsDAO:
    @staticmethod
    def find_all():
        return ScheduleSupplements.query.all()

    @staticmethod
    def find_by_id(schedule_supplement_id):
        schedule_supplement = ScheduleSupplements.query.get(schedule_supplement_id)
        if schedule_supplement:
            db.session.refresh(schedule_supplement)
        return schedule_supplement

    @staticmethod
    def find_by_schedule_id(schedule_id):
        return ScheduleSupplements.query.filter_by(schedule_id=schedule_id).all()

    @staticmethod
    def create(schedule_supplement):
        db.session.add(schedule_supplement)
        db.session.commit()
        return schedule_supplement

    @staticmethod
    def update(schedule_supplement_id, new_schedule_supplement):
        schedule_supplement = ScheduleSupplements.query.get(schedule_supplement_id)
        if schedule_supplement:
            for key, value in vars(new_schedule_supplement).items():
                if key != 'id' and value is not None:
                    setattr(schedule_supplement, key, value)
            db.session.commit()
        return schedule_supplement

    @staticmethod
    def patch(schedule_supplement_id, updates):
        schedule_supplement = ScheduleSupplements.query.get(schedule_supplement_id)
        if schedule_supplement:
            for key, value in updates.items():
                setattr(schedule_supplement, key, value)
            db.session.commit()
        return schedule_supplement

    @staticmethod
    def put(schedule_supplement_id, new_data):
        schedule_supplement = ScheduleSupplements.query.get(schedule_supplement_id)
        if schedule_supplement:
            for key in vars(schedule_supplement):
                if key != 'id':
                    setattr(schedule_supplement, key, new_data.get(key, None))
            db.session.commit()
        return schedule_supplement

    @staticmethod
    def delete(schedule_supplement_id):
        schedule_supplement = ScheduleSupplements.query.get(schedule_supplement_id)
        if schedule_supplement:
            db.session.delete(schedule_supplement)
            db.session.commit()
            return True
        return False

    @staticmethod
    def delete_all():
        ScheduleSupplements.query.delete()
        db.session.commit()
