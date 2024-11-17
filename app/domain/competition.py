from __future__ import annotations
from typing import Dict, Any
from app import db

class Competition(db.Model):
    __tablename__ = 'competition'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athlete.id'), nullable=False)

    # Зв'язок
    athlete = db.relationship('Athlete', back_populates='competitions')

    def __repr__(self) -> str:
        return f"Competition(id={self.id}, name={self.name}, date={self.date}, location={self.location}, athlete_id={self.athlete_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'location': self.location,
            'athlete_id': self.athlete_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Competition:
        return Competition(
            name=dto_dict.get('name'),
            date=dto_dict.get('date'),
            location=dto_dict.get('location'),
            athlete_id=dto_dict.get('athlete_id'),
        )
