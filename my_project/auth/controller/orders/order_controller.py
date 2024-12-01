"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.service import order_service
from my_project.auth.controller.general_controller import GeneralController


class OrderController(GeneralController):
    """
    Realisation of Order controller.
    """
    _service = order_service

    def get_orders_above_cost(self, min_cost: float) -> List[object]:
        """
        Gets Order objects with cost >= min_cost using Service layer as DTO objects.
        :param min_cost: cost value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_orders_above_cost(min_cost)))

    def find_by_status(self, status: str) -> List[object]:
        """
        Gets Order objects filtered by status using Service layer as DTO objects.
        :param status: status value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.find_by_status(status)))
