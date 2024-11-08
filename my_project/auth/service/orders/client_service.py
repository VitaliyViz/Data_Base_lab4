"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.dao import client_dao
from my_project.auth.service.general_service import GeneralService


class ClientService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = client_dao

    def get_clients_after_number(self, in_number: int) -> List[object]:
        """
        Gets Client objects from database table with field 'number' >= in_number.
        :param in_number: number value
        :return: list of all objects
        """
        return self._dao.get_clients_after_number(in_number)

    def get_clients_with_name_and_number_filter(self, name_filter: str, in_number: int) -> List[object]:
        """
        Gets Client objects from database table with name filter and field 'number' >= in_number.
        :param name_filter: first letters of name
        :param in_number: number value
        :return: list of all objects
        """
        return self._dao.get_clients_with_name_and_number_filter(name_filter, in_number)
