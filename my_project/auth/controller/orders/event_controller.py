from typing import List
from my_project.auth.service import event_service
from my_project.auth.controller.general_controller import GeneralController

class EventController(GeneralController):
    _service = event_service

    def find_by_address(self, address: str) -> List[object]:
        return list(map(lambda x: dict(x), self._service.find_by_address(address)))
