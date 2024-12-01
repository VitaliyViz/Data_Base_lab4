"""
2024
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.payment import Payment


class PaymentDAO(GeneralDAO):
    """
    Realisation of Payment data access layer.
    """
    _domain_type = Payment

    def find_by_order_id(self, order_id: int) -> List[object]:
        """
        Gets Payment objects from database table by field 'order_id'.
        :param order_id: Order ID value
        :return: search objects
        """
        return self._session.query(Payment).filter(Payment.order_id == order_id).order_by(Payment.payment_date.desc()).all()

    def find_by_status(self, status: str) -> List[object]:
        """
        Gets Payment objects from database table by field 'status'.
        :param status: Payment status
        :return: search objects
        """
        return self._session.query(Payment).filter(Payment.status == status).order_by(Payment.payment_date.desc()).all()
