from config import VACANCIES_PATH_TXT, VACANCIES_PATH_JSON
from src.json_saver import JSONSaver
from src.txt_saver import TXTSaver
from src.utils import user_choice_json, user_choice_txt


def main():
    """ Запуск программы """
    print("Здравствуйте!")
    while True:
        user_input = input("В каком формате хотите записать данные?\n"
                           "1 - json формат\n"
                           "2 - txt формат\n"
                           "3 - удалить данные из файла\n"
                           "4 - выйти из программы\n")

        if user_input == "1":
            user_choice_json()
        elif user_input == "2":
            user_choice_txt()
        elif user_input == "3":
            delete_data()
        elif user_input == "4":
            print("Выход из программы...")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1, 2, 3 или 4.")


def delete_data():
    """ Удаление данных из файла """
    user_input = input("Какой файл вы хотите отчистить?\n"
                       "1 - json-файл\n"
                       "2 - txt-файл\n")

    if user_input == "1":
        deleter = JSONSaver(VACANCIES_PATH_JSON)
        deleter.del_data()
        print("Данные из json файла удалены!")
    elif user_input == "2":
        deleter = TXTSaver(VACANCIES_PATH_TXT)
        deleter.del_data()
        print("Данные из txt файла удалены!")
    else:
        print("Некорректный ввод. Пожалуйста, выберите 1 или 2.")


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()

