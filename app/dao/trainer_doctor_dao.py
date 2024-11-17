from .. import db
from ..domain.trainer_doctor import TrainerDoctor

class TrainerDoctorDAO:
    @staticmethod
    def find_all():
        return TrainerDoctor.query.all()

    @staticmethod
    def find_by_id(trainer_doctor_id):
        trainer_doctor = TrainerDoctor.query.get(trainer_doctor_id)
        if trainer_doctor:
            db.session.refresh(trainer_doctor)
        return trainer_doctor

    @staticmethod
    def create(trainer_doctor):
        db.session.add(trainer_doctor)
        db.session.commit()
        return trainer_doctor

    @staticmethod
    def update(trainer_doctor_id, new_trainer_doctor):
        trainer_doctor = TrainerDoctor.query.get(trainer_doctor_id)
        if trainer_doctor:
            for key, value in vars(new_trainer_doctor).items():
                if key != 'id' and value is not None:
                    setattr(trainer_doctor, key, value)
            db.session.commit()
        return trainer_doctor

    @staticmethod
    def patch(trainer_doctor_id, updates):
        trainer_doctor = TrainerDoctor.query.get(trainer_doctor_id)
        if trainer_doctor:
            for key, value in updates.items():
                setattr(trainer_doctor, key, value)
            db.session.commit()
        return trainer_doctor

    @staticmethod
    def put(trainer_doctor_id, new_data):
        trainer_doctor = TrainerDoctor.query.get(trainer_doctor_id)
        if trainer_doctor:
            for key in vars(trainer_doctor):
                if key != 'id':
                    setattr(trainer_doctor, key, new_data.get(key, None))
            db.session.commit()
        return trainer_doctor

    @staticmethod
    def delete(trainer_doctor_id):
        trainer_doctor = TrainerDoctor.query.get(trainer_doctor_id)
        if trainer_doctor:
            db.session.delete(trainer_doctor)
            db.session.commit()
            return True
        return False

    @staticmethod
    def delete_all():
        TrainerDoctor.query.delete()
        db.session.commit()
