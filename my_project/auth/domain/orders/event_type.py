from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class EventType(db.Model, IDto):
    __tablename__ = "event_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    events = db.relationship('Event', backref='event_type', lazy=True)

    def __repr__(self) -> str:
        return f"EventType({self.id}, '{self.name}', '{self.address}', '{self.phone}', '{self.email}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EventType:
        return EventType(**dto_dict)
