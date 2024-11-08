from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Event(db.Model, IDto):
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_date = db.Column(db.Date, nullable=False)
    event_duration = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    total_cost = db.Column(db.Numeric(10, 2), nullable=False)
    event_type_id = db.Column(db.Integer, db.ForeignKey('event_type.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Event({self.id}, {self.event_date}, {self.event_duration}, '{self.address}', {self.total_cost}, {self.event_type_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "event_date": self.event_date,
            "event_duration": self.event_duration,
            "address": self.address,
            "total_cost": self.total_cost,
            "event_type_id": self.event_type_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Event:
        return Event(**dto_dict)
