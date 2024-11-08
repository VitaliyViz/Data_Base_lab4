from typing import List
from my_project.auth.service import animator_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.animator import Animator


class AnimatorController(GeneralController):
    """
    Реалізація контролера аніматорів.
    """
    _service = animator_service

    def create_animator(self, animator: Animator) -> None:
        """
        Створює нового аніматора в базі даних.
        :param animator: аніматор, якого потрібно створити
        """
        self._service.create(animator)

    def find_all(self) -> List[Animator]:
        """
        Отримує всіх аніматорів з бази даних.
        :return: список аніматорів
        """
        return self._service.get_all_animators()

    def find_by_id(self, animator_id: int) -> Animator:
        """
        Отримує аніматора за ID.
        :param animator_id: ID аніматора
        """
        return self._service.get_animator_by_id(animator_id)

    def update_animator(self, animator_id: int, animator: Animator) -> None:
        """
        Оновлює аніматора за ID.
        :param animator_id: ID аніматора
        :param animator: аніматор з новими даними
        """
        self._service.update(animator_id, animator)

    def delete_animator(self, animator_id: int) -> None:
        """
        Видаляє аніматора за ID.
        :param animator_id: ID аніматора
        """
        self._service.delete(animator_id)

    def get_animator_by_name(self, name: str) -> List[Animator]:
        """
        Отримує агенції за назвою.
        :param name: назва аніматора
        :return: список аніматорів з відповідною назвою
        """
        return self._service.get_animator_by_name(name)

    def get_animator_by_phone(self, phone: str) -> List[Animator]:
        """
        Отримує аніматора за номером телефону.
        :param phone: номер телефону аніматора
        :return: список аніматорів з відповідним телефоном
        """
        return self._service.get_animator_by_phone(phone)