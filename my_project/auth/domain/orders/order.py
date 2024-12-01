"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Order(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.Numeric(10, 2), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Order({self.id}, '{self.date}', '{self.status}', {self.cost}, {self.event_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "date": str(self.date),
            "status": self.status,
            "cost": float(self.cost),
            "event_id": self.event_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Order:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Order(**dto_dict)
        return obj
