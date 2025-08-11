class Vacancy:
    """ Класс для работы с вакансиями """

    __slots__ = ("name", "alternate_url", "salary_from", "salary_to", "area_name", "requirement", "responsibility")

    def __init__(self, name, alternate_url, salary_from, salary_to, area_name, requirement, responsibility):
        """ Конструктор класса """

        self.name: str = self.__validate_name(name)
        self.alternate_url: str = self.__validate_url(alternate_url)
        self.salary_from: int = self.__validate_salary(salary_from)
        self.salary_to: int = self.__validate_salary(salary_to)
        self.area_name: str = self.__validate_area_name(area_name)
        self.requirement: str = self.__validate_text(requirement)
        self.responsibility: str = self.__validate_text(responsibility)

    def validate_name(self, name: str) -> str:
        if not name or not isinstance(name, str):
            raise ValueError("Имя вакансии должно быть непустой строкой.")
        return name

    def validate_url(self, url: str) -> str:
        if not url.startswith("http://") and not url.startswith("https://"):
            raise ValueError("Ссылка на вакансию должна начинаться с http:// или https://")
        return url

    def validate_salary(self, salary: int) -> int:
        if not isinstance(salary, int) or salary < 0:
            raise ValueError("Зарплата должна быть неотрицательным целым числом.")
        return salary

    def validate_area_name(self, area_name: str) -> str:
        if not area_name or not isinstance(area_name, str):
            raise ValueError("Название региона должно быть непустой строкой.")
        return area_name

    def validate_text(self, text: str) -> str:
        if not isinstance(text, str):
            raise ValueError("Описание должно быть строкой.")
        return text

    def __str__(self) -> str:
        """ Строковое представление вакансии """

        return (f"Наименование вакансии: {self.name}\n"
                f"Ссылка на вакансию: {self.alternate_url}\n"
                f"Зарплата: от {self.salary_from} до {self.salary_to}\n"
                f"Место работы: {self.area_name}\n"
                f"Краткое описание: {self.requirement}\n"
                f"{self.responsibility}\n")

    def __lt__(self, other) -> bool:
        """ Метод сравнения от большего к меньшему """

        return self.salary_from < other.salary_from

    @classmethod
    def from_hh_dict(cls, vacancy_data: dict):
        """ Метод возвращает экземпляр класса в виде списка """

        salary = vacancy_data.get("salary")

        return cls(
            vacancy_data["name"],
            vacancy_data["alternate_url"],
            salary.get("from") if salary.get("from") else 0,
            salary.get("to") if salary.get("to") else 0,
            vacancy_data["area"]["name"],
            vacancy_data["snippet"]["requirement"],
            vacancy_data["snippet"]["responsibility"],
        )

    def to_dict(self) -> dict:
        """ Метод возвращает вакансию в виде словаря """

        return {
            "name": self.name,
            "alternate_url": self.alternate_url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "area_name": self.area_name,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
        }