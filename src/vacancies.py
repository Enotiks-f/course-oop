class Vacancy:

    def __init__(self, vac):
        self.name: str = vac.get("url", "Ссылка отсутствует")
        self.url: str = vac.get("alternate_url")
        self.salary: str = self._validation_salary(vac.get("salary"))
        self.description: str = self._get_description(vac.get("snippet"))


    def to_dict(self):
        """Преобразование объекта вакансии в словарь для сохранения."""
        return {
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "description": self.description
        }



    def _get_description(self, description):
        """Получение описания из snippet и возвращает requirement и responsibility
        """
        requirement = description.get("requirement", "")
        responsibility = description.get("responsibility", "")
        desc = requirement
        if responsibility:
            desc += " " + responsibility
        return desc.strip() if desc else "Описание отсутствует"


    def _validation_salary(self, salary):
        """Валидация salary"""
        if salary is None:
            self.salary_from = 0
            self.salary_to = 0
            return f"{self.salary_from} - {self.salary_to} руб."
        else:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0
            return f"{self.salary_from} - {self.salary_to} руб."

    def __eq__(self, other):
        if isinstance(other, Vacancy):
            return self.salary_from == other.salary_from
        elif isinstance(other, int):
            return self.salary_from == other
        raise TypeError("Сравнение возможно только с Vacancy или int")

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary_from < other.salary_from
        elif isinstance(other, int):
            return self.salary_from < other
        raise TypeError("Сравнение возможно только с Vacancy или int")

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary_from > other.salary_from
        elif isinstance(other, int):
            return self.salary_from > other
        raise TypeError("Сравнение возможно только с Vacancy или int")

    def __le__(self, other):
        if isinstance(other, Vacancy):
            return self.salary_from <= other.salary_from
        elif isinstance(other, int):
            return self.salary_from <= other
        raise TypeError("Сравнение возможно только с Vacancy или int")

    def __ge__(self, other):
        if isinstance(other, Vacancy):
            return self.salary_from >= other.salary_from
        elif isinstance(other, int):
            return self.salary_from >= other
        raise TypeError("Сравнение возможно только с Vacancy или int")

    def __str__(self):
        return f"{self.name}, {self.url}, {self.salary}, {self.description}"

