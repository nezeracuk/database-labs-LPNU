from __future__ import annotations
from typing import Dict, Any
from app import db

class TrainerDoctor(db.Model):
    __tablename__ = 'trainer_doctor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    contact_info = db.Column(db.String(255), nullable=False, unique=True)

    # Зв'язки
    schedules = db.relationship('Schedule', back_populates='trainer_doctor', lazy='dynamic')
    schedule_supplements = db.relationship('ScheduleSupplements', back_populates='trainer_doctor', lazy='dynamic')
    trainer_has_athlete = db.relationship('Athlete', secondary='athlete_trainer', back_populates='athlete_has_trainer')

    def __repr__(self) -> str:
        return f"TrainerDoctor(id={self.id}, firstname={self.firstname}, lastname={self.lastname}, contact_info={self.contact_info})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'contact_info': self.contact_info,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TrainerDoctor:
        return TrainerDoctor(
            firstname=dto_dict.get('firstname'),
            lastname=dto_dict.get('lastname'),
            contact_info=dto_dict.get('contact_info'),
        )

    @staticmethod
    def insert_dummy_data():
        for i in range(1, 11):
            dummy_trainer = TrainerDoctor(
                firstname=f"Noname{i}",
                lastname=f"Trainer{i}",
                contact_info=f"contact{i}@example.com"
            )
            db.session.add(dummy_trainer)
        db.session.commit()
