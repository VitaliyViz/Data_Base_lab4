from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.animator_agency import AnimatorAgency

class AnimatorAgencyDAO(GeneralDAO):
    """
    DAO for AnimatorAgency.
    """
    _domain_type = AnimatorAgency

    def find_by_animator_id(self, animator_id: int) -> List[AnimatorAgency]:
        """
        Gets all agency relationships for a given animator ID.
        """
        return self._session.query(AnimatorAgency).filter(AnimatorAgency.animator_id == animator_id).all()

    def find_by_agency_id(self, agency_id: int) -> List[AnimatorAgency]:
        """
        Gets all animator relationships for a given agency ID.
        """
        return self._session.query(AnimatorAgency).filter(AnimatorAgency.agency_id == agency_id).all()
    def get_all(self) -> List[AnimatorAgency]:
        """
        Gets all relationships in the animator_agency table.
        """
        return self._session.query(AnimatorAgency).all()