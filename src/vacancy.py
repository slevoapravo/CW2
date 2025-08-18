class Vacancy:
    """ Класс для работы с вакансиями """

    __slots__ = ("name", "alternate_url", "salary_from", "salary_to", "area_name", "requirement", "responsibility")

    def __init__(self, name, alternate_url, salary_from, salary_to, area_name, requirement, responsibility):
        """ Конструктор класса """
        self.name: str = self.validate_name(name)
        self.alternate_url: str = self.validate_url(alternate_url)
        self.salary_from: int = self._validate_salary(salary_from)
        self.salary_to: int = self._validate_salary(salary_to)
        self.area_name: str = self.validate_area_name(area_name)
        self.requirement: str = self.validate_text(requirement)
        self.responsibility: str = self.validate_text(responsibility)

    def validate_name(self, name: str) -> str:
        if not name or not isinstance(name, str):
            raise ValueError("Имя вакансии должно быть непустой строкой.")
        return name

    def validate_url(self, url: str) -> str:
        if not url.startswith("http://") and not url.startswith("https://"):
            raise ValueError("Ссылка на вакансию должна начинаться с http:// или https://")
        return url

    def _validate_salary(self, salary: int) -> int:
        """ Приватный метод для валидации зарплаты """
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
        """ Метод возвращает экземпляр класса из словаря вакансии """
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

    # Метод get_response (например, в классе, который обрабатывает API запросы)
    def get_response(self, keyword, per_page) -> 'Response':
        self.params["text"] = keyword
        self.params["per_page"] = per_page
        response = requests.get(self.url, params=self.params)

        if response.status_code == 200:
            return response
        else:
                        response.raise_for_status()