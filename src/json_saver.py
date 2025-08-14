import json

# Определение переменной для пути к json-файлу
TEST_VACANCIES_PATH_JSON = "tests/tests_data/vacancies.json"

class Saver:
    """ Базовый класс для сохранения данных. """
    pass  # Здесь можно добавить общий функционал для сохранителей

class JSONSaver(Saver):
    """ Класс для записи в json-файл """

    def __init__(self, filename=TEST_VACANCIES_PATH_JSON):
        """ Конструктор класса """
        self.__filename = filename  # Приватный атрибут

    def write_data(self, vacancies):
        """ Запись данных в json """
        data = self.get_data()
        data.extend(vacancies)

        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_data(self):
        """ Получение данных json """
        try:
            with open(self.__filename, encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def del_data(self):
        """ Удаление данных из файла """
        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)