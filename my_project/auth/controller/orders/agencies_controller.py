from typing import List
from my_project.auth.service import agencies_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.agencies import Agencies


class AgenciesController(GeneralController):
    """
    Реалізація контролера агентств.
    """
    _service = agencies_service

    def create_agency(self, agency: Agencies) -> None:
        """
        Створює нову агенцію в базі даних.
        :param agency: агенція, яку потрібно створити
        """
        self._service.create(agency)

    def find_all(self) -> List[Agencies]:
        """
        Отримує всі агенції з бази даних.
        :return: список агентств
        """
        return self._service.get_all_agencies()

    def find_by_id(self, agency_id: int) -> Agencies:
        """
        Отримує агенцію за ID.
        :param agency_id: ID агенції
        :return: агенція
        """
        return self._service.get_agency_by_id(agency_id)

    def update_agency(self, agency_id: int, agency: Agencies) -> None:
        """
        Оновлює агенцію за ID.
        :param agency_id: ID агенції
        :param agency: агенція з новими даними
        """
        self._service.update(agency_id, agency)

    def delete_agency(self, agency_id: int) -> None:
        """
        Видаляє агенцію за ID.
        :param agency_id: ID агенції
        """
        self._service.delete(agency_id)

    def get_agencies_by_name(self, name: str) -> List[Agencies]:
        """
        Отримує агенції за назвою.
        :param name: назва агенції
        :return: список агентств з відповідною назвою
        """
        return self._service.get_agencies_by_name(name)

    def get_agencies_by_phone(self, phone: str) -> List[Agencies]:
        """
        Отримує агенції за номером телефону.
        :param phone: номер телефону агенції
        :return: список агентств з відповідним телефоном
        """
        return self._service.get_agencies_by_phone(phone)