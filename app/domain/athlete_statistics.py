from __future__ import annotations
from typing import Dict, Any
from app import db
from sqlalchemy import event, select

class AthleteStatistics(db.Model):
    __tablename__ = 'athlete_statistics'

    athlete_id = db.Column(db.Integer, db.ForeignKey('athlete.id', ondelete='CASCADE', onupdate='CASCADE'),primary_key=True)
    total_competitions = db.Column(db.Integer, nullable=False)
    best_score = db.Column(db.Numeric(5, 2), nullable=False)
    average_score = db.Column(db.Numeric(5, 2), nullable=False)

    def __repr__(self):
        return f"AthleteStatistics(athlete_id={self.athlete_id}, total_competitions={self.total_competitions}, best_score={self.best_score}, average_score={self.average_score})"

    def put_into_dto(self):
        return {
            "athlete_id": self.athlete_id,
            "total_competitions": self.total_competitions,
            "best_score": float(self.best_score),
            "average_score": float(self.average_score)
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AthleteStatistics:
        return AthleteStatistics(
            athlete_id=dto_dict.get('athlete_id'),
            total_competitions=dto_dict.get('total_competitions'),
            best_score=dto_dict.get('best_score'),
            average_score=dto_dict.get('average_score')
        )

@event.listens_for(AthleteStatistics, "before_insert")
def check_team_from_to(mapper, connection, target):
    athlete_statistics = db.Table('athlete', db.metadata, autoload_with=db.engine)

    athlete_exists = connection.execute(
        select(athlete_statistics.c.id).where(athlete_statistics.c.id == target.athlete_id)
    ).first()

    if not athlete_exists:
        raise ValueError(f"Athlete with id {target.athlete_id} does not exist in athletes table.")
