from abc import ABC, abstractmethod

from src.dto import Vacancy


class FileConnector(ABC):
    @abstractmethod
    def get_vacancies(self) -> list[Vacancy]:
        """Абстрактный метод для получения вакансий без обязательных атрибутов"""
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        """Абстрактный метод для добавления вакансий без обязательных атрибутов"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        """Абстрактный метод для удаления вакансий без обязательных атрибутов"""
        pass
