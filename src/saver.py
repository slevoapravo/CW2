from abc import ABC, abstractmethod


class Saver(ABC):
    """ Абстрактный класс для записи в файл """


    @abstractmethod
    def write_data(self, vacancies):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def del_data(self):
        pass
