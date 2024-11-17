from __future__ import annotations
from typing import Dict, Any, List
from app import db

class Athlete(db.Model):
    __tablename__ = 'athlete'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    height = db.Column(db.Numeric(5, 2))
    weight = db.Column(db.Numeric(5, 2))

    # Зв'язки
    competitions = db.relationship('Competition', back_populates='athlete', lazy='dynamic')
    schedules = db.relationship('Schedule', back_populates='athlete', lazy='dynamic')
    athlete_has_trainer = db.relationship('TrainerDoctor', secondary='athlete_trainer', back_populates='trainer_has_athlete' )

    def __repr__(self) -> str:
        return f"Athlete(id={self.id}, firstname={self.firstname}, lastname={self.lastname}, height={self.height}, weight={self.weight})"

    def put_into_dto(self) -> Dict[str, Any]:
        athlete_has_trainer = [athlete_has_traine.put_into_dto() for athlete_has_traine in self.athlete_has_trainer]
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'height': self.height,
            'weight': self.weight,
            'competitions': [comp.put_into_dto() for comp in self.competitions],
            'schedules': [schedule.put_into_dto() for schedule in self.schedules],
            'athlete_has_trainer': athlete_has_trainer if athlete_has_trainer else None,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Athlete:
        return Athlete(
            firstname=dto_dict.get('firstname'),
            lastname=dto_dict.get('lastname'),
            height=dto_dict.get('height'),
            weight=dto_dict.get('weight'),
        )
