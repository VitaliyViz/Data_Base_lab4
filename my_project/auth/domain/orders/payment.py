"""
2024
apavelchak@gmail.com
© Andrii Pavelchak
"""
from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Payment(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "payment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, nullable=True)
    payment_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    payment_method = db.Column(db.String(50), nullable=True)
    status = db.Column(db.String(30), nullable=True)

    def __repr__(self) -> str:
        return f"Payment({self.id}, '{self.order_id}', '{self.payment_date}', {self.amount}, '{self.payment_method}', '{self.status}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "order_id": self.order_id,
            "payment_date": self.payment_date.isoformat(),
            "amount": float(self.amount),
            "payment_method": self.payment_method or "",
            "status": self.status or "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Payment:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Payment(**dto_dict)
        return obj
