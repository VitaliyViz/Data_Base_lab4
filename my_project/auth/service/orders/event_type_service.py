from typing import List
from my_project.auth.dao import event_type_dao
from my_project.auth.service.general_service import GeneralService

class EventTypeService(GeneralService):
    _dao = event_type_dao

    def find_by_name(self, name: str) -> List[object]:
        return self._dao.find_by_name(name)

    def find_by_email(self, email: str) -> List[object]:
        return self._dao.find_by_email(email)
