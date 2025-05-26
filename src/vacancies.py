from abc import ABC, abstractmethod

import requests


class VacancyAPI(ABC):
    base_url: str
    def __init__(self, base_url):
        self.base_url = base_url


    @abstractmethod
    def get_vacancies(self):
        pass

class HeadHunterAPI(VacancyAPI):
    def __init__(self):
        super().__init__("https://api.hh.ru/vacancies")

    def get_vacancies(self, params=None):
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



class Vacancy:

    def __init__(self, name, url, salary, description):
        self.name: str = name
        self.url: str = url
        self.salary: int = self._validation_salary(salary)
        self.description: str = description

    def _validation_salary(self, salary):
        if  salary is None or isinstance(salary, int) and salary <= 0:
            return 0
        return salary

    def __eq__(self, other):
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("")

        ob = other if isinstance(other, int) else other.salary
        return self.salary == ob

    def __lt__(self, other):
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("\033[31mМожно сравнивать только с объектами Vacancy или числами\033[0m")

        ob = other if isinstance(other, int) else other.salary
        return self.salary < ob

    def __gt__(self, other):
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("\033[31mМожно сравнивать только с объектами Vacancy или числами\033[0m")

        ob = other if isinstance(other, int) else other.salary
        return self.salary > ob

    def __le__(self, other):
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("\033[31mМожно сравнивать только с объектами Vacancy или числами\033[0m")

        ob = other if isinstance(other, int) else other.salary
        return self.salary <= ob

    def __ge__(self, other):
        if not isinstance(other, (Vacancy, int)):
            raise TypeError("\033[31mМожно сравнивать только с объектами Vacancy или числами\033[0m")

        ob = other if isinstance(other, int) else other.salary
        return self.salary >= ob

    def __str__(self):
        return f"{self.name}, {self.url}, {self.salary}, {self.description}"

if __name__ == "__main__":
    hh = HeadHunterAPI()
    vacancies = hh.get_vacancies(params={"text": "python"})
    for i in vacancies:
         print(i)
