from pathlib import Path

from src.api_clients import HeadHunterApi
from src.api_clients.base import VacancyApiClient
from src.file_connector import JsonConnector
from src.file_connector.base import FileConnector


BASE_PATH = Path(__file__).parent
VACANCIES_PATH_FILE = BASE_PATH.joinpath('vacancies.json')

api_client: VacancyApiClient = HeadHunterApi()
json_connector: FileConnector = JsonConnector(VACANCIES_PATH_FILE)

WELCOME_MESSAGE = """
Добро пожаловать в программу. Выберите действие: 
1. Загрузить вакансии в файл по ключевому слову
2. Вывести Ваш топ вакансий из файла
0. Выйти
"""


def download_vacancy_by_key_word():
    search_word = input("Введите ключевое слово для поиска: ")
    vacancies = api_client.get_vacancies(search_word.lower())
    for vacancy in vacancies:
        json_connector.add_vacancy(vacancy)
        print(vacancy)


def show_top_n_vacancies_from_file():
    vacancies = json_connector.get_vacancies()
    for vacancy in \
            (sorted(vacancies,
                    key=lambda x: x.salary,
                    reverse=True))[:int(input('Введите сколько лучших вакансий вывести из списка: '))]:
        print(vacancy)


def main():
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
