from typing import List, Optional
from .. import db
from ..domain.athlete_trainer import AthleteTrainer


class AthleteTrainerDAO:
    @staticmethod
    def find_all():
        """
        Отримати всі записи зі стикувальної таблиці.
        """
        return AthleteTrainer.query.all()

    @staticmethod
    def find_by_id(athlete_id, trainer_doctor_id):
        """
        Отримати запис за ID атлета та тренера.
        """
        return AthleteTrainer.query.filter_by(
            athlete_id=athlete_id, trainer_doctor_id=trainer_doctor_id
        ).first()

    @staticmethod
    def create(athlete_trainer):
        """
        Створити новий запис у стикувальній таблиці.
        """
        db.session.add(athlete_trainer)
        db.session.commit()
        return athlete_trainer

    @staticmethod
    def create_all(athlete_trainer_list):
        """
        Створити кілька записів у стикувальній таблиці.
        """
        db.session.bulk_save_objects(athlete_trainer_list)
        db.session.commit()
        return athlete_trainer_list

    @staticmethod
    def delete(athlete_id, trainer_doctor_id):
        """
        Видалити запис за ID атлета та тренера.
        """
        athlete_trainer = AthleteTrainerDAO.find_by_id(athlete_id, trainer_doctor_id)
        if athlete_trainer:
            db.session.delete(athlete_trainer)
            db.session.commit()
            return True
        return False

    @staticmethod
    def delete_all():
        """
        Видалити всі записи зі стикувальної таблиці.
        """
        AthleteTrainer.query.delete()
        db.session.commit()

    @staticmethod
    def find_trainers_by_athlete(athlete_id):
        """
        Отримати всіх тренерів для атлета.
        """
        return AthleteTrainer.query.filter_by(athlete_id=athlete_id).all()

    @staticmethod
    def find_athletes_by_trainer(trainer_doctor_id):
        """
        Отримати всіх атлетів для тренера.
        """
        return AthleteTrainer.query.filter_by(trainer_doctor_id=trainer_doctor_id).all()

    @staticmethod
    def put(athlete_id, trainer_doctor_id, new_data: dict):
        """
        Повністю оновити запис.
        """
        athlete_trainer = AthleteTrainerDAO.find_by_id(athlete_id, trainer_doctor_id)
        if athlete_trainer:
            # Повністю оновлюємо поля
            if 'athlete_id' in new_data and new_data['athlete_id'] is not None:
                athlete_trainer.athlete_id = new_data['athlete_id']
            if 'trainer_doctor_id' in new_data and new_data['trainer_doctor_id'] is not None:
                athlete_trainer.trainer_doctor_id = new_data['trainer_doctor_id']
            db.session.commit()
        return athlete_trainer

    @staticmethod
    def patch(athlete_id, trainer_doctor_id, updates: dict):
        """
        Частково оновити запис.
        """
        athlete_trainer = AthleteTrainerDAO.find_by_id(athlete_id, trainer_doctor_id)
        if athlete_trainer:
            # Оновлюємо лише вказані поля
            if 'athlete_id' in updates and updates['athlete_id'] is not None:
                athlete_trainer.athlete_id = updates['athlete_id']
            if 'trainer_doctor_id' in updates and updates['trainer_doctor_id'] is not None:
                athlete_trainer.trainer_doctor_id = updates['trainer_doctor_id']
            db.session.commit()
        return athlete_trainer
