import requests
from abc import ABC, abstractmethod

class GetVacanciesAPI:
    """Базовый класс для получения вакансий, может содержать общую логику."""

    pass

class HeadHunterAPI(GetVacanciesAPI, ABC):
    """Абстрактный класс для работы с API HeadHunter."""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "per_page": "", "only_with_salary": True}

    @abstractmethod
    def get_vacancies(self, keyword: str, per_page: int):
        response = self.get_response(keyword, per_page)
        return response["items"]

class RealHeadHunterAPI(HeadHunterAPI):
    """Реализация API HeadHunter."""

    def get_response(self, keyword: str, per_page: int) -> dict:
        self._HeadHunterAPI__params["text"] = keyword
        self._HeadHunterAPI__params["per_page"] = per_page
        response = requests.get(self._HeadHunterAPI__url, headers=self._HeadHunterAPI__headers, params=self._HeadHunterAPI__params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Ошибка при получении данных: {response.status_code} - {response.text}")