from typing import List
from my_project.auth.service import event_type_service
from my_project.auth.controller.general_controller import GeneralController

class EventTypeController(GeneralController):
    _service = event_type_service

    def find_by_name(self, name: str) -> List[object]:
        return list(map(lambda x: dict(x), self._service.find_by_name(name)))

    def find_by_email(self, email: str) -> List[object]:
        return list(map(lambda x: dict(x), self._service.find_by_email(email)))
