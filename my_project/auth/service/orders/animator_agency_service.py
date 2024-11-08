from typing import List
from my_project.auth.dao import animator_agency_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.animator_agency import AnimatorAgency

class AnimatorAgencyService(GeneralService):
    """
    Service layer for AnimatorAgency.
    """
    _dao = animator_agency_dao

    def get_animators_by_agency(self, agency_id: int) -> List[AnimatorAgency]:
        """
        Gets all animator relationships for a specific agency.
        """
        return self._dao.find_by_agency_id(agency_id)

    def get_agencies_by_animator(self, animator_id: int) -> List[AnimatorAgency]:
        """
        Gets all agency relationships for a specific animator.
        """
        return self._dao.find_by_animator_id(animator_id)
    def get_all_relationships(self) -> List[AnimatorAgency]:
        """
        Gets all relationships in the animator_agency table.
        """
        return self._dao.get_all()