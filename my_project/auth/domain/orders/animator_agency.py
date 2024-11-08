from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class AnimatorAgency(db.Model, IDto):
    """
    Model declaration for AnimatorAgency as a junction table.
    """
    __tablename__ = "animator_agency"

    animator_id = db.Column(db.Integer, db.ForeignKey('animator.id'), primary_key=True)
    agency_id = db.Column(db.Integer, db.ForeignKey('agencies.id'), primary_key=True)

    def __repr__(self) -> str:
        return f"AnimatorAgency(animator_id={self.animator_id}, agency_id={self.agency_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO format.
        :return: DTO object as dictionary
        """
        return {
            "animator_id": self.animator_id,
            "agency_id": self.agency_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AnimatorAgency:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        return AnimatorAgency(**dto_dict)
