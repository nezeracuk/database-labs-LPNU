from __future__ import annotations
from typing import Dict, Any
from app import db

class Ingredient(db.Model):
    __tablename__ = 'ingredient'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    quantity = db.Column(db.String(100), nullable=False)
    unit = db.Column(db.String(50), nullable=False)

    # Зв'язки
    meal_ingredients = db.relationship('MealIngredients', back_populates='ingredient', lazy='dynamic')

    def __repr__(self) -> str:
        return f"Ingredient(id={self.id}, name={self.name}, description={self.description}, quantity={self.quantity}, unit={self.unit})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'quantity': self.quantity,
            'unit': self.unit,
            'meal_ingredients': [mi.put_into_dto() for mi in self.meal_ingredients]
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Ingredient:
        return Ingredient(
            name=dto_dict.get('name'),
            description=dto_dict.get('description'),
            quantity=dto_dict.get('quantity'),
            unit=dto_dict.get('unit'),
        )
