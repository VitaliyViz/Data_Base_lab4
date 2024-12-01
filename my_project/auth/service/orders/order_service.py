"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.dao import order_dao
from my_project.auth.service.general_service import GeneralService


class OrderService(GeneralService):
    """
    Realisation of Order service.
    """
    _dao = order_dao

    def get_orders_above_cost(self, min_cost: float) -> List[object]:
        """
        Gets Order objects from database table where cost >= min_cost.
        :param min_cost: cost value
        :return: list of all objects
        """
        return self._dao.get_orders_above_cost(min_cost)

    def find_by_status(self, status: str) -> List[object]:
        """
        Gets Order objects filtered by status.
        :param status: status value
        :return: list of all objects
        """
        return self._dao.find_by_status(status)
