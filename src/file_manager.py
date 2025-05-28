from abc import ABC, abstractmethod
import os
import json

class BaseFileManger(ABC):

    @abstractmethod
    def add_file(self, data):
        pass

    @abstractmethod
    def get_data_file(self):
        pass

    @abstractmethod
    def del_vacancy_id(self, vacancy):
        pass

class FileManeger(BaseFileManger):
    def __init__(self, file_pach="data/vacancies.json"):
        self.file_pach = file_pach


    def add_file(self, data):
        """Добавляет ваканскии в json file"""
        try:
            with open(self.file_pach, "r", encoding="utf-8") as f:
                old_data = json.load(f)
            for i in data:
                id_vacancies = i.get("id", "ID")
                old_data[id_vacancies] = i
        except json.JSONDecodeError:
            old_data = {}

            old_data = {}
        with open(self.file_pach, "w",  encoding="utf-8") as f:
            json.dump(old_data, f, ensure_ascii=False, indent=2)


    def get_data_file(self):
        """Получает вакансии из json"""
        with open(self.file_pach, "r",  encoding="utf-8") as f:
            json.load(f)

    def del_vacancy_id(self, vacancy):
        """Удаляет вакансии по id"""
        try:
            with open(self.file_pach, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}

        if vacancy in data:
             del data[vacancy]


        with open(self.file_pach, "w",  encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
