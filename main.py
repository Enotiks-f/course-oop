from src.vacancies import Vacancy, HeadHunterAPI
from src.user_func import filter_vacancies_by_description, get_top_n_vacancies

def main():
    hh = HeadHunterAPI()

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

        elif choice == "0":
            print("Выход.")
            break

        else:
            print("Неверный ввод. Попробуйте снова.")


main()

