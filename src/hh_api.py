from abc import ABC, abstractmethod

import requests

class VacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass

class HeadHunterAPI(VacancyAPI):
    def __init__(self):
        self.base_url: str = "https://api.hh.ru/vacancies"

    def get_vacancies(self, params=None):
        """Подключаеся к api и возвращает вакансии"""
        try:
            req = requests.get(self.base_url, params=params)
            if req.status_code == 200:
                return req.json().get("items")
            else:
                print(f"Ошибка запроса: {req.status_code}")
                return []
        except requests.RequestException as e:
            print(f"Ошибка при запросе: {e}")
            return []

    def get_vacancy_detail(self, vacancy_id):
        url = f"https://api.hh.ru/vacancies/{vacancy_id}"
        response = requests.get(url)
        return response.json()

if __name__ == "__main__":
    hh = HeadHunterAPI()
    v = hh.get_vacancies()
    for i in v:
        print(i)