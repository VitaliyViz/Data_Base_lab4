
from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Agencies(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "agencies"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    address = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"Agencies({self.id}, '{self.name}', '{self.address}', '{self.phone}', '{self.email}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Agencies:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        # obj = Client(
        #     name=dto_dict.get("name"),
        #     number=dto_dict.get("number"),
        #     client_type_id=dto_dict.get("client_type_id")
        # )
        obj = Agencies(**dto_dict)
        return obj
