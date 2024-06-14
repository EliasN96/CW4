from pathlib import Path

from prettytable import PrettyTable

from src.api_clients import HeadHunterApi
from src.api_clients.base import VacancyApiClient
from src.file_connector import JsonConnector
from src.file_connector.base import FileConnector


# Создание экземпляра класса, который будет создавать файл для вакансий и добавлять их туда
BASE_PATH = Path(__file__).parent
VACANCIES_PATH_FILE = BASE_PATH.joinpath('vacancies.json')

# Создание экземпляра класса для работы с API сайтов с вакансиями
api_client: VacancyApiClient = HeadHunterApi()
json_connector: FileConnector = JsonConnector(VACANCIES_PATH_FILE)

# Приветственное сообщение с выбором действий
WELCOME_MESSAGE = """
Добро пожаловать в программу. Выберите действие: 
1. Загрузить вакансии в файл по ключевому слову
2. Вывести n-количество(будет задано Вами далее) вакансий из файла 
0. Выйти
"""


def download_vacancy_by_key_word():
    """Функция для загрузки вакансии по ключевому слову"""
    search_word = input("Введите ключевое слово для поиска: ")
    # Получение вакансий с hh.ru в формате JSON
    vacancies = api_client.get_vacancies(search_word.lower())
    for vacancy in vacancies:
        json_connector.add_vacancy(vacancy)
        print(vacancy)


def show_top_n_vacancies_from_file():
    """Функция для отображения заданного пользователем кол-ва лучших вакансий из файла,
    отсортированных от лучших по зарплате к менее привлекательным"""
    vacancies = json_connector.get_vacancies()
    pt = PrettyTable(['Название вакансии', 'Ссылка на вакансию', 'Работадатель', 'Зарплата(от -> до, валюта)'])
    for vacancy in \
            (sorted(vacancies,
                    key=lambda x: x.salary,
                    reverse=True))[:int(input('Введите сколько лучших вакансий вывести из списка: '))]:
        salary = '{_from} -> {_to}, {_currency}'.format(
            _from=vacancy.salary.salary_from or "Не указано",
            _to=vacancy.salary.salary_to or "Не указано",
            _currency=vacancy.salary.currency
        )
        pt.add_row([vacancy.name, vacancy.url, vacancy.employer_name, salary])
    print(pt)


def main():
    """Главный метод, который запускает программу"""
    while True:
        print(WELCOME_MESSAGE)
        user_input = input()
        if not user_input.isdigit():
            continue

        if int(user_input) == 0:
            break
        elif int(user_input) == 1:
            download_vacancy_by_key_word()
        elif int(user_input) == 2:
            show_top_n_vacancies_from_file()


if __name__ == "__main__":
    main()
