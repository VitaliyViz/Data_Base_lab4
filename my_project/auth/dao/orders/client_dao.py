"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.client import Client
import sqlalchemy


class ClientDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Client

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Client objects from database table by field name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Client).filter(Client.name == name).order_by(Client.name).all()

    def find_by_number(self, number: int) -> List[object]:
        """
        Gets Client objects from database table by field 'number'.
        :param number: number value
        :return: search objects
        """
        return self._session.query(Client).filter(Client.number == number).order_by(Client.number.desc()).all()

    # STORED PROCEDUREs
    def get_clients_after_number(self, in_num: int) -> List[object]:
        """
        Gets Client objects from database table with field 'number' >= in_number.
        :param in_num: number value
        :return: search objects
        """
        return self._session.execute(sqlalchemy.text("CALL get_clients_after_number(:p1)"),
                                     {"p1": in_num}).mappings().all()

    def get_clients_with_name_and_number_filter(self, name_filter: str, in_num: int) -> List[object]:
        """
        Gets Client objects from database table with name filter and field 'number' >= in_number.
        :param name_filter: first letters of name
        :param in_num: number value
        :return: search objects
        """
        return self._session.execute(sqlalchemy.text("CALL get_clients_with_name_and_number_filter(:p1, :p2)"),
                                     {"p1": name_filter, "p2": in_num}).mappings().all()
