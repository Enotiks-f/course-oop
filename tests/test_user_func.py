import unittest
from src.vacancies import Vacancy
from src.user_func import filter_vacancies_by_description, get_top_n_vacancies

sample_vacancy_dict = {
    "id": "123",
    "name": "Python Developer",
    "alternate_url": "http://example.com",
    "salary": {"from": 100000, "to": 150000},
    "snippet": {"requirement": "Python", "responsibility": "Backend development"}
}

sample_vacancy_dict_2 = {
    "id": "124",
    "name": "Junior Developer",
    "alternate_url": "http://example.com/junior",
    "salary": {"from": 50000, "to": 70000},
    "snippet": {"requirement": "Fast learner", "responsibility": "Support"}
}

class TestUserFunctions(unittest.TestCase):
    def setUp(self):
        self.v1 = Vacancy(sample_vacancy_dict)
        self.v2 = Vacancy(sample_vacancy_dict_2)
        self.vacancies = [self.v1, self.v2]

    def test_filter_by_description(self):
        result = filter_vacancies_by_description(self.vacancies, "Python")
        self.assertEqual(len(result), 1)
        self.assertIn("Python", result[0].description)

    def test_get_top_n_vacancies(self):
        top_1 = get_top_n_vacancies(self.vacancies, 1)
        self.assertEqual(top_1[0], self.v1)
