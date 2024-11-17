from __future__ import annotations
from typing import Dict, Any
from app import db

class Schedule(db.Model):
    __tablename__ = 'schedule'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.String(45), nullable=False)
    end_date = db.Column(db.String(45), nullable=False)
    frequency = db.Column(db.String(45))
    athlete_id = db.Column(db.Integer, db.ForeignKey('athlete.id'), nullable=False)
    trainer_doctor_id = db.Column(db.Integer, db.ForeignKey('trainer_doctor.id'), nullable=False)
    schedule_meal_id = db.Column(db.Integer, db.ForeignKey('schedule_meal.id'), nullable=False)
    schedule_supplements_id = db.Column(db.Integer, db.ForeignKey('schedule_supplements.id'), nullable=False)

    # Зв'язки
    athlete = db.relationship('Athlete', back_populates='schedules')
    trainer_doctor = db.relationship('TrainerDoctor', back_populates='schedules')
    schedule_meal = db.relationship('ScheduleMeal', back_populates='schedules')
    schedule_supplements = db.relationship('ScheduleSupplements', back_populates='schedules')

    def __repr__(self) -> str:
        return f"Schedule(id={self.id}, start_date={self.start_date}, end_date={self.end_date}, frequency={self.frequency}, athlete_id={self.athlete_id}, trainer_doctor_id={self.trainer_doctor_id}, schedule_meal_id={self.schedule_meal_id}, schedule_supplements_id={self.schedule_supplements_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'frequency': self.frequency,
            'athlete_id': self.athlete_id,
            'trainer_doctor_id': self.trainer_doctor_id,
            'schedule_meal_id': self.schedule_meal_id,
            'schedule_supplements_id': self.schedule_supplements_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Schedule:
        return Schedule(
            start_date=dto_dict.get('start_date'),
            end_date=dto_dict.get('end_date'),
            frequency=dto_dict.get('frequency'),
            athlete_id=dto_dict.get('athlete_id'),
            trainer_doctor_id=dto_dict.get('trainer_doctor_id'),
            schedule_meal_id=dto_dict.get('schedule_meal_id'),
            schedule_supplements_id=dto_dict.get('schedule_supplements_id'),
        )
