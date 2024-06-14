import requests


class TestVacancyLink:
    """Тестирование работы ссылки hh.ru"""
    def test_correct_link(self):
        link = 'https://api.hh.ru/vacancies/'
        response = requests.get(link)
        assert response.status_code == 200

    def test_incorrect_link(self):
        link = 'https://apii.hh.ru/vacancies/'
        response = requests.get(link)
        assert response.status_code == 404
