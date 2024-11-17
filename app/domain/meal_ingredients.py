from __future__ import annotations
from typing import Dict, Any
from app import db

class MealIngredients(db.Model):
    __tablename__ = 'meal_ingredients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantity = db.Column(db.Numeric(10, 2), nullable=False)
    unit = db.Column(db.String(45), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), nullable=False)
    meal_schedule_meal_id = db.Column(db.Integer, db.ForeignKey('schedule_meal.id'), nullable=False)

    # Зв'язки
    ingredient = db.relationship('Ingredient', back_populates='meal_ingredients')
    meal = db.relationship('Meal', back_populates='meal_ingredients')

    def __repr__(self) -> str:
        return f"MealIngredients(id={self.id}, quantity={self.quantity}, unit={self.unit}, ingredient_id={self.ingredient_id}, meal_id={self.meal_id}, meal_schedule_meal_id={self.meal_schedule_meal_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'quantity': self.quantity,
            'unit': self.unit,
            'ingredient_id': self.ingredient_id,
            'meal_id': self.meal_id,
            'meal_schedule_meal_id': self.meal_schedule_meal_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> MealIngredients:
        return MealIngredients(
            quantity=dto_dict.get('quantity'),
            unit=dto_dict.get('unit'),
            ingredient_id=dto_dict.get('ingredient_id'),
            meal_id=dto_dict.get('meal_id'),
            meal_schedule_meal_id=dto_dict.get('meal_schedule_meal_id'),
        )
