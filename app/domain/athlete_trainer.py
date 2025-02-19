from __future__ import annotations
from typing import Dict, Any
from app import db
from .athlete import Athlete
from .trainer_doctor import TrainerDoctor


class AthleteTrainer(db.Model):
    __tablename__ = 'athlete_trainer'

    athlete_id = db.Column(db.Integer, db.ForeignKey('athlete.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    trainer_doctor_id = db.Column(db.Integer, db.ForeignKey('trainer_doctor.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)

    def __repr__(self) -> str:
        return f"AthleteTrainer(athlete_id={self.athlete_id}, trainer_doctor_id={self.trainer_doctor_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Convert the object into a dictionary suitable for a DTO (Data Transfer Object).
        """
        return {
            'athlete_id': self.athlete_id,
            'trainer_doctor_id': self.trainer_doctor_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AthleteTrainer:
        """
        Create an AthleteTrainer object from a DTO dictionary.
        """
        return AthleteTrainer(
            athlete_id=dto_dict.get('athlete_id'),
            trainer_doctor_id=dto_dict.get('trainer_doctor_id')
        )

    @staticmethod
    def add_athlete_trainer(athlete_name: str, trainer_doctor_name: int) -> AthleteTrainer:
        athlete = Athlete.query.filter_by(firstname=athlete_name).first()
        if not athlete:
            raise ValueError("Athlete not found")

        trainer_doctor = TrainerDoctor.query.filter_by(firstname=trainer_doctor_name).first()
        if not trainer_doctor:
            raise ValueError("Trainer_doctor not found")

        athlete_trainer_doctor = AthleteTrainer(athlete_id=athlete.id, trainer_doctor_id=trainer_doctor.id)
        db.session.add(athlete_trainer_doctor)
        db.session.commit()
        return athlete_trainer_doctor


