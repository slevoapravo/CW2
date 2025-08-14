from src.saver import Saver

class TXTSaver(Saver):
    """ Класс для записи в txt-файл """

    def __init__(self, filename):
        """ Конструктор класса """
        super().__init__(filename)  # Вызов конструктора базового класса

    def write_data(self, vacancies):
        """ Запись данных в txt """
        with open(self.filename, "a", encoding="utf-8") as file:
            for vacancy in vacancies:
                file.write(f"{vacancy}\n")

    def get_data(self):
        """ Получение данных из txt """
        with open(self.filename, encoding="utf-8") as file:
            return file.readlines()

    def del_data(self):
        """ Удаление данных из файла """
        with open(self.filename, "w", encoding="utf-8"):
            pass

