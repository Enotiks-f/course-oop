from src.vacancies import Vacancy

def filter_vacancies_by_description(vacancies: list[Vacancy], string_search: str) -> list[Vacancy]:
    """Возвращает вакансии по ключывым словам в описании"""
    return [vacancy for vacancy in vacancies if string_search in vacancy.description]

def get_top_n_vacancies(vacancies, n):
    """Возвращает топ N вакансий по убыванию зарплаты (salary_from)."""
    return sorted(vacancies, key=lambda v: v.salary_from, reverse=True)[:n]
