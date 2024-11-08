"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from my_project.auth.service import client_type_service
from my_project.auth.controller.general_controller import GeneralController


class ClientTypeController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = client_type_service
