"""
2022-2023
apavelchak@gmail.com
© Andrii Pavelchak
"""
from typing import List

from my_project.auth.service import client_service
from my_project.auth.controller.general_controller import GeneralController


class ClientController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = client_service

    def get_clients_after_number(self, in_number: int) -> List[object]:
        """
        Gets Client objects from database table with field 'number' >= in_number using Service layer as DTO objects.
        :param in_number: number value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_clients_after_number(in_number)))

    def get_clients_with_name_and_number_filter(self, name_filter: str, in_number: int) -> List[object]:
        """
        Gets Client objects from database table with name filter and field 'number' >= in_number
        using Service layer as DTO objects.
        :param name_filter: first letters of name
        :param in_number: number value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_clients_with_name_and_number_filter(name_filter,
                                                                                                 in_number)))
