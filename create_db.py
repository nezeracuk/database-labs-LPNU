#!/usr/bin/env python3
"""
Простий скрипт для створення всіх таблиць в базі даних
"""
import sys
import os

# Додаємо шлях до проекту
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.database import db

# Імпортуємо всі моделі, щоб SQLAlchemy їх знав
from app.domain.athlete import Athlete
from app.domain.athlete_statistics import AthleteStatistics
from app.domain.athlete_trainer import AthleteTrainer
from app.domain.competition import Competition
from app.domain.ingredient import Ingredient
from app.domain.meal import Meal
from app.domain.meal_ingredients import MealIngredients
from app.domain.schedule import Schedule
from app.domain.schedule_meal import ScheduleMeal
from app.domain.schedule_supplements import ScheduleSupplements
from app.domain.supplement import Supplement
from app.domain.trainer_doctor import TrainerDoctor

def create_tables():
    """Створює всі таблиці в базі даних"""
    print("=" * 60)
    print("Створення таблиць в базі даних skibytskyi2")
    print("=" * 60)
    
    app = create_app()
    
    with app.app_context():
        try:
            # Створюємо всі таблиці
            print("\nСтворюю таблиці...")
            db.create_all()
            print("✓ Всі таблиці успішно створені!")
            
            # Показуємо список створених таблиць
            print("\nСписок таблиць:")
            for table in db.metadata.sorted_tables:
                print(f"  - {table.name}")
            
            print("\n" + "=" * 60)
            print("Готово! Тепер можете запустити додаток: python3 app.py")
            print("=" * 60)
            
        except Exception as e:
            print(f"✗ Помилка при створенні таблиць: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)

if __name__ == '__main__':
    create_tables()

