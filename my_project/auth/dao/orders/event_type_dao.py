from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.event_type import EventType

class EventTypeDAO(GeneralDAO):
    _domain_type = EventType

    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(EventType).filter(EventType.name == name).all()
    
    def find_by_email(self, email: str) -> List[object]:
        return self._session.query(EventType).filter(EventType.email == email).all()
