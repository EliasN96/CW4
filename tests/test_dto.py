from src.dto import Salary


class TestSalaryCompare:
    def test_salary_are_equals_none_with_same_currency(self):
        """
        Тест с одинаковыми от и до - зарплатами, а также валютой
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
        lower_salary = Salary(salary_from=40000, salary_to=60000, currency='RUR')
        higher_salary = Salary(salary_from=40000, salary_to=70000, currency='RUR')
        assert lower_salary.salary_to < higher_salary.salary_to
