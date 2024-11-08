from typing import List
from my_project.auth.dao import agencies_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.agencies import Agencies

class AgenciesService(GeneralService):
    """
    Реалізація сервісу агентств.
    """
    _dao = agencies_dao

    def create(self, agency: Agencies) -> None:
        """
        Створює нову агенцію в базі даних.
        :param agency: агенція, яку потрібно створити
        """
        self._dao.create(agency)

    def update(self, agency_id: int, agency: Agencies) -> None:
        """
        Оновлює агенцію в базі даних.
        :param agency_id: ID агенції
        :param agency: агенція з новими даними
        """
        self._dao.update(agency_id, agency)

    def get_all_agencies(self) -> List[Agencies]:
        """
        Отримує всі агенції з бази даних.
        :return: список всіх агенцій
        """
        return self._dao.find_all()

    def get_agency_by_id(self, agency_id: int) -> Agencies:
        """
        Отримує агенцію за ID.
        :param agency_id: ID агенції
        :return: агенція
        """
        return self._dao.find_by_id(agency_id)

    def get_agencies_by_name(self, name: str) -> List[Agencies]:
        """
        Отримує агентства з таблиці бази даних за назвою.
        :param name: значення назви агентства
        :return: список агентств з відповідною назвою
        """
        return self._dao.find_by_name(name)

    def get_agencies_by_phone(self, phone: str) -> List[Agencies]:
        """
        Отримує агентства з таблиці бази даних за номером телефону.
        :param phone: значення телефону агентства
        :return: список агентств з відповідним телефоном
        """
        return self._dao.find_by_phone(phone)