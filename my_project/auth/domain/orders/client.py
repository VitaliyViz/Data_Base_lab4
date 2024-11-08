# """
# 2022
# apavelchak@gmail.com
# © Andrii Pavelchak
# """

# from __future__ import annotations
# from typing import Dict, Any

# from my_project import db
# from my_project.auth.domain.i_dto import IDto


# class Client(db.Model, IDto):
#     """
#     Model declaration for Data Mapper.
#     """
#     __tablename__ = "client"

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(30))
#     number = db.Column(db.Integer)

#     # Relationship 1:M
#     client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
#     client_type = db.relationship("ClientType", backref="clients")  # only on the child class

#     def __repr__(self) -> str:
#         return f"Client({self.id}, '{self.name}', '{self.number}', '{self.client_type}')"

#     def put_into_dto(self) -> Dict[str, Any]:
#         """
#         Puts domain object into DTO without relationship
#         :return: DTO object as dictionary
#         """
#         return {
#             "id": self.id,
#             "name": self.name,
#             "number": self.number,
#             "client_type_id": self.client_type_id or "",
#             "client_type": self.client_type.type if self.client_type is not None else "",
#         }

#     @staticmethod
#     def create_from_dto(dto_dict: Dict[str, Any]) -> Client:
#         """
#         Creates domain object from DTO
#         :param dto_dict: DTO object
#         :return: Domain object
#         """
#         # obj = Client(
#         #     name=dto_dict.get("name"),
#         #     number=dto_dict.get("number"),
#         #     client_type_id=dto_dict.get("client_type_id")
#         # )
#         obj = Client(**dto_dict)
#         return obj
