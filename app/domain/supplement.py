from __future__ import annotations
from typing import Dict, Any
from app import db

class Supplement(db.Model):
    __tablename__ = 'supplement'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    dosage = db.Column(db.String(100), nullable=False)
    frequency = db.Column(db.String(100), nullable=False)
    schedule_supplements_id = db.Column(db.Integer, db.ForeignKey('schedule_supplements.id'), nullable=False)

    # Зв'язки
    schedule_supplements = db.relationship('ScheduleSupplements', back_populates='supplements')

    def __repr__(self) -> str:
        return f"Supplement(id={self.id}, name={self.name}, description={self.description}, dosage={self.dosage}, frequency={self.frequency}, schedule_supplements_id={self.schedule_supplements_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'dosage': self.dosage,
            'frequency': self.frequency,
            'schedule_supplements_id': self.schedule_supplements_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Supplement:
        return Supplement(
            name=dto_dict.get('name'),
            description=dto_dict.get('description'),
            dosage=dto_dict.get('dosage'),
            frequency=dto_dict.get('frequency'),
            schedule_supplements_id=dto_dict.get('schedule_supplements_id'),
        )
