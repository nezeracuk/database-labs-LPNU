from __future__ import annotations
from typing import Dict, Any
from app import db

class ScheduleMeal(db.Model):
    __tablename__ = 'schedule_meal'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meal_name = db.Column(db.String(255), nullable=False)
    day_of_week = db.Column(db.Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
    meal_time = db.Column(db.Enum('Breakfast', 'Lunch', 'Dinner'))
    ServingSize = db.Column(db.String(100), nullable=False)

    # Зв'язки
    meals = db.relationship('Meal', back_populates='schedule_meal')
    schedules = db.relationship('Schedule', back_populates='schedule_meal', lazy='dynamic')

    def __repr__(self) -> str:
        return f"ScheduleMeal(id={self.id}, meal_name={self.meal_name}, day_of_week={self.day_of_week}, meal_time={self.meal_time}, ServingSize={self.ServingSize})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'meal_name': self.meal_name,
            'day_of_week': self.day_of_week,
            'meal_time': self.meal_time,
            'ServingSize': self.ServingSize,
            'meals': [meal.put_into_dto() for meal in self.meals],
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ScheduleMeal:
        return ScheduleMeal(
            meal_name=dto_dict.get('meal_name'),
            day_of_week=dto_dict.get('day_of_week'),
            meal_time=dto_dict.get('meal_time'),
            ServingSize=dto_dict.get('ServingSize'),
        )
