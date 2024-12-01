"""
2024
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.service import payment_service
from my_project.auth.controller.general_controller import GeneralController


class PaymentController(GeneralController):
    """
    Realisation of Payment controller.
    """
    _service = payment_service

    def find_by_order_id(self, order_id: int) -> List[object]:
        """
        Gets Payment objects by Order ID using Service layer as DTO objects.
        :param order_id: Order ID
        :return: list of objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.find_by_order_id(order_id)))

    def find_by_status(self, status: str) -> List[object]:
        """
        Gets Payment objects by Status using Service layer as DTO objects.
        :param status: Payment status
        :return: list of objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.find_by_status(status)))
