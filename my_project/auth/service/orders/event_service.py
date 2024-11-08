from typing import List
from my_project.auth.dao import event_dao
from my_project.auth.service.general_service import GeneralService

class EventService(GeneralService):
    _dao = event_dao

    def find_by_address(self, address: str) -> List[object]:
        return self._dao.find_by_address(address)
