import unittest
from unittest.mock import patch, MagicMock
from src.hh_api import HeadHunterAPI

mock_vacancy_list = {
    "items": [
        {"id": "1", "name": "Python Developer"},
        {"id": "2", "name": "Data Scientist"},
    ]
}

mock_vacancy_detail = {
    "id": "1",
    "name": "Python Developer",
    "description": "Detailed job info here"
}

class TestHeadHunterAPI(unittest.TestCase):
    @patch("requests.get")
    def test_get_vacancies_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_vacancy_list
        mock_get.return_value = mock_response

        hh = HeadHunterAPI()
        vacancies = hh.get_vacancies()

        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[0]["name"], "Python Developer")
        mock_get.assert_called_with(hh.base_url, params=None)

    @patch("requests.get")
    def test_get_vacancies_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        hh = HeadHunterAPI()
        result = hh.get_vacancies()
        self.assertEqual(result, [])

    @patch("requests.get")
    def test_get_vacancy_detail(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = mock_vacancy_detail
        mock_get.return_value = mock_response

        hh = HeadHunterAPI()
        detail = hh.get_vacancy_detail("1")

        self.assertEqual(detail["name"], "Python Developer")
        mock_get.assert_called_with("https://api.hh.ru/vacancies/1")
