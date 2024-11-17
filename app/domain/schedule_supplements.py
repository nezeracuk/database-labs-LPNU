from __future__ import annotations
from typing import Dict, Any
from app import db

class ScheduleSupplements(db.Model):
    __tablename__ = 'schedule_supplements'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    supplement_name = db.Column(db.String(255), nullable=False)
    dosage = db.Column(db.String(100))
    time_of_day = db.Column(db.Enum('Morning', 'Afternoon', 'Evening'))
    duration = db.Column(db.String(100))
    trainer_doctor_id = db.Column(db.Integer, db.ForeignKey('trainer_doctor.id'), nullable=True)

    # Зв'язки
    trainer_doctor = db.relationship('TrainerDoctor', back_populates='schedule_supplements')
    schedules = db.relationship('Schedule', back_populates='schedule_supplements')
    supplements = db.relationship('Supplement', back_populates='schedule_supplements', lazy='dynamic')

    def __repr__(self) -> str:
        return f"ScheduleSupplements(id={self.id}, supplement_name={self.supplement_name}, dosage={self.dosage}, time_of_day={self.time_of_day}, duration={self.duration})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'supplement_name': self.supplement_name,
            'dosage': self.dosage,
            'time_of_day': self.time_of_day,
            'duration': self.duration,
            'trainer_doctor_id': self.trainer_doctor_id,
            'supplements': [supplement.put_into_dto() for supplement in self.supplements]
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ScheduleSupplements:
        return ScheduleSupplements(
            supplement_name=dto_dict.get('supplement_name'),
            dosage=dto_dict.get('dosage'),
            time_of_day=dto_dict.get('time_of_day'),
            duration=dto_dict.get('duration'),
            trainer_doctor_id=dto_dict.get('trainer_doctor_id'),
        )
