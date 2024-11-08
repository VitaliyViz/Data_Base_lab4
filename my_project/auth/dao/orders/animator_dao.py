from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.animator import Animator

class AnimatorDAO(GeneralDAO):
    """
    Реалізація рівня доступу даних для аніматорів.
    """
    _domain_type = Animator

    def create(self, animator: Animator) -> None:
        """
        Додає нового аніматора в базу даних.
        :param animator: аніматор, якого потрібно додати
        """
        self._session.add(animator)
        self._session.commit()

    def find_all(self) -> List[Animator]:
        """
        Отримує всіх аніматорів з таблиці бази даних.
        :return: список всіх аніматорів
        """
        return self._session.query(Animator).all()

    def find_by_name(self, name: str) -> List[Animator]:
        """
        Отримує аніматора з таблиці бази даних за полем name.
        :param name: значення назви
        :return: знайдені об'єкти
        """
        return self._session.query(Animator).filter(Animator.name == name).order_by(Animator.name).all()

    def find_by_phone(self, phone: str) -> List[Animator]:
        """
        Отримує аніматорів з таблиці бази даних за полем 'phone'.
        :param phone: значення телефону
        :return: знайдені об'єкти
        """
        return self._session.query(Animator).filter(Animator.phone == phone).order_by(Animator.phone.desc()).all()

    def find_by_id(self, animator_id: int) -> Animator:
        """
        Отримує аніматора за ID.
        :param animator_id: ID агенції
        :return: animator
        """
        return self._session.query(Animator).filter(Animator.id == animator_id).first()
    