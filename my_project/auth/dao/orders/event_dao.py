
from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.event import Event

class EventDAO(GeneralDAO):
    _domain_type = Event

    def find_by_address(self, address: str) -> List[object]:
        return self._session.query(Event).filter(Event.address == address).all()

    # Add more DAO methods for specific queries if needed
