from __future__ import annotations
from typing import Dict, Any
from app import db
from sqlalchemy.sql import func
from sqlalchemy import Enum

class Meal(db.Model):
    __tablename__ = 'meal'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.Text, nullable=False)
    energy_value = db.Column(db.Numeric(10, 2))
    meal_type = db.Column(Enum('Breakfast', 'Lunch', 'Dinner'))
    schedule_meal_id = db.Column(db.Integer, db.ForeignKey('schedule_meal.id'), nullable=False)

    # Зв'язки
    schedule_meal = db.relationship('ScheduleMeal', back_populates='meals')
    meal_ingredients = db.relationship('MealIngredients', back_populates='meal', lazy='dynamic')

    def __repr__(self) -> str:
        return f"Meal(id={self.id}, name={self.name}, description={self.description}, energy_value={self.energy_value}, meal_type={self.meal_type}, schedule_meal_id={self.schedule_meal_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'energy_value': self.energy_value,
            'meal_type': self.meal_type,
            'schedule_meal_id': self.schedule_meal_id,
            'meal_ingredients': [mi.put_into_dto() for mi in self.meal_ingredients]
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Meal:
        return Meal(
            name=dto_dict.get('name'),
            description=dto_dict.get('description'),
            energy_value=dto_dict.get('energy_value'),
            meal_type=dto_dict.get('meal_type'),
            schedule_meal_id=dto_dict.get('schedule_meal_id'),
        )

    @staticmethod
    def get_min_energy() -> float:
        """
        Отримати мінімальне значення енергетичної цінності.
        """
        return db.session.query(func.min(Meal.energy_value)).scalar()

    @staticmethod
    def get_max_energy() -> float:
        """
        Отримати максимальне значення енергетичної цінності.
        """
        return db.session.query(func.max(Meal.energy_value)).scalar()

    @staticmethod
    def get_sum_energy() -> float:
        """
        Отримати сумарне значення енергетичної цінності.
        """
        return db.session.query(func.sum(Meal.energy_value)).scalar()

    @staticmethod
    def get_avg_energy() -> float:
        """
        Отримати середнє значення енергетичної цінності.
        """
        return db.session.query(func.avg(Meal.energy_value)).scalar()

def insert_meal(name: str, description: str, energy_value: float, meal_type: str, schedule_meal_id: int) -> Meal:
    new_meal = Meal(
        name=name,
        description=description,
        energy_value=energy_value,
        meal_type=meal_type,
        schedule_meal_id=schedule_meal_id
    )
    db.session.add(new_meal)
    db.session.commit()
    return new_meal



