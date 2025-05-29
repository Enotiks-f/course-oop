import unittest
from src.vacancies import Vacancy

sample_vacancy_dict = {
    "id": "123",
    "name": "Python Developer",
    "alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=120583586",
    "salary": {"from": 100000, "to": 150000},
    "snippet": {"requirement": "Python", "responsibility": "Backend development"}
}

sample_vacancy_dict_2 = {
    "id": "124",
    "name": "Junior Developer",
    "alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=120583586",
    "salary": {"from": 50000, "to": 70000},
    "snippet": {"requirement": "Fast learner", "responsibility": "Support"}
}

class TestVacancy(unittest.TestCase):
    def test_vacancy_init(self):
        vac = Vacancy(sample_vacancy_dict)
        self.assertEqual(vac.salary_from, 100000)
        self.assertEqual(vac.salary_to, 150000)
        self.assertIn("Python", vac.description)

    def test_vacancy_comparison(self):
        v1 = Vacancy(sample_vacancy_dict)
        v2 = Vacancy(sample_vacancy_dict_2)
        self.assertTrue(v1 > v2)
        self.assertTrue(v1 >= v2)
        self.assertFalse(v1 == v2)
        self.assertTrue(v2 < v1)
        self.assertTrue(v2 <= v1)
        self.assertTrue(v1 == 100000)
