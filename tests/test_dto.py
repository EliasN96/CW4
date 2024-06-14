import pytest

from src.dto import Salary


class TestSalaryCompare:
    """Класс с методами для автоматического тестирования зарплаты"""
    def test_salary_are_equals_none_with_same_currency(self):
        """
        Тест с одинаковыми от и до - зарплатами(None), а также валютой
        """
        salary_1 = Salary(salary_from=None, salary_to=None, currency='RUR')
        salary_2 = Salary(salary_from=None, salary_to=None, currency='RUR')
        assert salary_1 == salary_2

    def test_salary_are_equals_none_with_different_currency(self):
        """
        Тест с одинаковыми от и до - зарплатами(None), но разной валютой
        """
        salary_1 = Salary(salary_from=None, salary_to=None, currency='RUR')
        salary_2 = Salary(salary_from=None, salary_to=None, currency='USD')
        assert salary_1 != salary_2

    def test_salary_are_equals_not_none_with_same_currency(self):
        """
        Тест с одинаковыми от и до - зарплатами, а также валютой
        """
        salary_1 = Salary(salary_from=40000, salary_to=70000, currency='USD')
        salary_2 = Salary(salary_from=40000, salary_to=70000, currency='USD')
        assert salary_1 == salary_2

    def test_salary_are_equals_not_none_with_different_currency(self):
        """
        Тест с одинаковыми от и до - зарплатами, но разной валютой
        """
        salary_1 = Salary(salary_from=40000, salary_to=70000, currency='RUR')
        salary_2 = Salary(salary_from=40000, salary_to=70000, currency='USD')
        assert salary_1 != salary_2

    def test_same_from_salaries_to_salary_equal_none(self):
        """
        Тест с разной минимальной зарплатой
        """
        lower_salary = Salary(salary_from=40000, salary_to=None, currency='RUR')
        higher_salary = Salary(salary_from=50000, salary_to=None, currency='RUR')
        assert lower_salary.salary_from < higher_salary.salary_from

    def test_same_to_salaries_from_salary_equal_none(self):
        """
        Тест с разной максимальной зарплатой
        """
        lower_salary = Salary(salary_from=None, salary_to=60000, currency='RUR')
        higher_salary = Salary(salary_from=None, salary_to=70000, currency='RUR')
        assert lower_salary.salary_to < higher_salary.salary_to

    def test_equal_salary_from(self):
        """
        Тест с одинаковой минимальной зарплатой
        """
        salary_1 = Salary(salary_from=50000, salary_to=60000, currency='RUR')
        salary_2 = Salary(salary_from=50000, salary_to=70000, currency='RUR')
        assert salary_1.salary_from == salary_2.salary_from

    def test_equal_salary_to(self):
        """
        Тест с одинаковой максимальной зарплатой
        """
        salary_1 = Salary(salary_from=40000, salary_to=70000, currency='RUR')
        salary_2 = Salary(salary_from=50000, salary_to=70000, currency='RUR')
        assert salary_1.salary_to == salary_2.salary_to

    def test_salary_from_less_than_salary_to(self):
        """
        Тест максимальной зарплаты выше минимальной
        """
        salary = Salary(salary_from=50000, salary_to=70000, currency='RUR')
        assert salary.salary_to > salary.salary_from

    def test_salary_from_more_than_salary_to(self):
        """
        Тест минимальной зарплаты выше максимальной
        """
        with pytest.raises(ArithmeticError) as ar:
            salary = Salary(salary_from=70000, salary_to=50000, currency='RUR')
            assert salary.min_salary_more_than_max_salary() == ar


