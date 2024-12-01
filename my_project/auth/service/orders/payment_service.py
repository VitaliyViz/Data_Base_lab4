"""
2024
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.dao import payment_dao
from my_project.auth.service.general_service import GeneralService


class PaymentService(GeneralService):
    """
    Realisation of Payment service.
    """
    _dao = payment_dao

    def find_by_order_id(self, order_id: int) -> List[object]:
        """
        Gets Payment objects by Order ID.
        :param order_id: Order ID
        :return: list of all matching objects
        """
        return self._dao.find_by_order_id(order_id)

    def find_by_status(self, status: str) -> List[object]:
        """
        Gets Payment objects by Status.
        :param status: Payment status
        :return: list of all matching objects
        """
        return self._dao.find_by_status(status)
