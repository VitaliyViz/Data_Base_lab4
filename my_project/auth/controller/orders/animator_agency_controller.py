from typing import List
from my_project.auth.service import animator_agency_service
from my_project.auth.controller.general_controller import GeneralController

class AnimatorAgencyController(GeneralController):
    """
    Controller for AnimatorAgency.
    """
    _service = animator_agency_service


    def get_animators_by_agency(self, agency_id: int) -> List[dict]:
        """
        Retrieves all animator relationships for a specific agency as DTOs.
        """
        return [animator_agency.put_into_dto() for animator_agency in self._service.get_animators_by_agency(agency_id)]

    def get_agencies_by_animator(self, animator_id: int) -> List[dict]:
        """
        Retrieves all agency relationships for a specific animator as DTOs.
        """
        return [animator_agency.put_into_dto() for animator_agency in self._service.get_agencies_by_animator(animator_id)]
    def get_all_relationships(self) -> List[dict]:
        """
        Retrieves all relationships in the animator_agency table as DTOs.
        """
        return [animator_agency.put_into_dto() for animator_agency in self._service.get_all_relationships()]