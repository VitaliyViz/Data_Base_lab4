"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List
from sqlalchemy import text

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.order import Order


class OrderDAO(GeneralDAO):
    """
    Realisation of Order data access layer.
    """
    _domain_type = Order

    def find_by_status(self, status: str) -> List[object]:
        """
        Gets Order objects from database table by field 'status'.
        :param status: status value
        :return: search objects
        """
        return self._session.query(Order).filter(Order.status == status).order_by(Order.date).all()

    def find_by_event_id(self, event_id: int) -> List[object]:
        """
        Gets Order objects from database table by field 'event_id'.
        :param event_id: event_id value
        :return: search objects
        """
        return self._session.query(Order).filter(Order.event_id == event_id).order_by(Order.id.desc()).all()

    def get_orders_above_cost(self, min_cost: float) -> List[object]:
        """
        Gets Order objects from database table where cost >= min_cost.
        :param min_cost: cost value
        :return: search objects
        """
        return self._session.execute(
            text("CALL get_orders_above_cost(:min_cost)"),
            {"min_cost": min_cost}
        ).mappings().all()
