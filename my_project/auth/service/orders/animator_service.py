from typing import List
from my_project.auth.dao import animator_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.animator import Animator

class AnimatorService(GeneralService):
    """
    Реалізація сервісу агентств.
    """
    _dao = animator_dao

    def create(self, animator: Animator) -> None:
        """
        Створює нового аніматора в базі даних.
        :param animator: аніматор, якого потрібно створити
        """
        self._dao.create(animator)

    def update(self, animator_id: int, animator: Animator) -> None:
        """
        Оновлює Аніматора в базі даних.
        :param animator_id: ID аніматора
        :param animator: аніматор з новими даними
        """
        self._dao.update(animator_id, animator)

    def get_all_animators(self) -> List[Animator]:
        """
        Отримує всіх аніматорів з бази даних.
        :return: список всіх аніматорів
        """
        return self._dao.find_all()

    def get_animator_by_id(self, animator_id: int) -> Animator:
        """
        Отримує аніматора за ID.
        :param animator_id: ID аніматора
        :return: аніматор
        """
        return self._dao.find_by_id(animator_id)

    def get_animator_by_name(self, name: str) -> List[Animator]:
        """
        Отримує аніматора з таблиці бази даних за назвою.
        :param name: значення назви аніматора
        :return: список аніматорів з відповідною назвою
        """
        return self._dao.find_by_name(name)

    def get_animator_by_phone(self, phone: str) -> List[Animator]:
        """
        Отримує аніматора з таблиці бази даних за номером телефону.
        :param phone: значення телефону аніматора
        :return: список аніматорів з відповідним телефоном
        """
        return self._dao.find_by_phone(phone)