from src.vacancies import Vacancy
from src.hh_api import HeadHunterAPI
from src.user_func import filter_vacancies_by_description, get_top_n_vacancies
from src.file_manager import FileManeger  # <-- подключение
import os

def main():
    hh = HeadHunterAPI()
    fm = FileManeger()

    print("=== Поиск вакансий на hh.ru ===")

    query = input("Введите поисковый запрос (например, 'python'): ").strip()
    raw_vacancies = hh.get_vacancies(params={"text": query})

    vacancies = []
    for item in raw_vacancies:
        vacancy = Vacancy(item)
        vacancies.append(vacancy)

    print(f"Найдено {len(vacancies)} вакансий.")

    while True:
        print("\nВыберите действие:")
        print("1. Показать топ N вакансий по зарплате")
        print("2. Найти вакансии по ключевому слову в описании")
        print("3. Показать все вакансии")
        print("4. Сохранить вакансии в файл")
        print("5. Удалить вакансию по ID")
        print("6. Показать вакансии из файла")
        print("0. Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            try:
                n = int(input("Введите количество вакансий: "))
                top_vacancies = get_top_n_vacancies(vacancies, n)
                for v in top_vacancies:
                    print(v)
            except ValueError:
                print("Ошибка: введите целое число.")

        elif choice == "2":
            keyword = input("Введите ключевое слово для поиска в описании: ").strip()
            filtered = filter_vacancies_by_description(vacancies, keyword)
            for v in filtered:
                print(v)

        elif choice == "3":
            for v in vacancies:
                print(v)

        elif choice == "4":
            to_save = [v.to_dict() for v in vacancies]
            fm.add_file(to_save)
            print("Вакансии сохранены в файл.")

        elif choice == "5":
            vac_id = input("Введите ID вакансии для удаления: ").strip()
            fm.del_vacancy_id(vac_id)
            print(f"Вакансия с ID {vac_id} удалена (если существовала).")

        elif choice == "6":
            try:
                with open(fm.file_pach, encoding="utf-8") as f:
                    data = f.read()
                    print(data)
            except FileNotFoundError:
                print("Файл не найден.")

        elif choice == "0":
            print("Выход.")
            break

        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
