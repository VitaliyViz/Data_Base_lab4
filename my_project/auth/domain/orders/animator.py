from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Animator(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "animator"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(100))
    gender = db.Column(db.String(20), nullable =True)
    birth_date = db.Column(db.Date, nullable =True)
    experience_years = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"Animator({self.id}, '{self.name}', '{self.last_name}', '{self.phone}', '{self.email}', '{self.gender}', '{self.birth_date}', '{self.experience_years}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "phone": self.phone,
            "email": self.email,
            "gender": self.gender,
            "birth_date": str(self.birth_date),
            "experience_years": self.experience_years,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Animator:
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
        obj = Animator(**dto_dict)
        return obj
