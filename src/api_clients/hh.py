import requests

from .base import VacancyApiClient
from ..dto import Vacancy, Salary


def _parse_vacancy_data(data: dict) -> Vacancy:
    """Метод для структурирования полученной информации"""
    return Vacancy(
        name=data['name'],
        url=data['alternate_url'],
        employer_name=data['employer']['name'],
        salary=Salary(
            salary_from=data['salary']['from'],
            salary_to=data['salary']['to'],
            currency=data['salary']['currency']
        )
    )


class HeadHunterApi(VacancyApiClient):
    """Класс наследующийся от абстрактного"""

    def get_vacancies(self, search_text: str) -> list[Vacancy]:
        """Метод для получения вакансий по ключевому слову"""
        url = 'https://api.hh.ru/vacancies/'
        params = {'only_with_salary': True,
                  'per_page': 100,
                  'text': search_text}

        response = requests.get(url, params=params, timeout=10)
        if not response.ok:
            print(f'ошибка получения данных с hh.ru, {response.content}')
            return []
        return [
            _parse_vacancy_data(item)
            for item in response.json()['items']
        ]

