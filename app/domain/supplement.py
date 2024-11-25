from __future__ import annotations
from typing import Dict, Any
from app import db
from datetime import datetime
from random import randint, choice
from sqlalchemy.sql import text

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

    @staticmethod
    def create_dynamic_tables_meal():
        supplement_names = db.session.query(Supplement.name).all()

        table_count = 0

        for name_tuple in supplement_names:
            if table_count >= 10:
                break

            supplement_name = name_tuple[0].replace(" ", "_")
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            table_name = f"{supplement_name}_{timestamp}"

            num_columns = randint(1, 9)

            columns_sql = []
            for i in range(1, num_columns + 1):
                col_name = f"col_{i}"
                col_type = choice(["VARCHAR(255)", "INT", "DECIMAL(10,2)", "DATE"])
                columns_sql.append(f"{col_name} {col_type}")

            columns_sql_str = ", ".join(columns_sql)
            create_table_sql = f"CREATE TABLE `{table_name}` (id INT AUTO_INCREMENT PRIMARY KEY, {columns_sql_str});"

            db.session.execute(text(create_table_sql))
            print(f"Created table: {table_name}")

            table_count += 1

        db.session.commit()


