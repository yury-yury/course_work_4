from typing import List, Dict, Any, Optional
import requests

from functions import dict_to_instance
from parser.abstract_parser import AbstractParser
from vacancies.vacancy import Vacancy


class HeadHunterParser(AbstractParser):
    """
    The HeadHunterParser class inherits from the AbstractParser abstract class. Designed to request the
    HeadHunter service API and get vacancies.
    """
    base_url: str = 'https://api.hh.ru/vacancies'
    headers: Dict[str, str] = {"User_Agent": "HHScalperApp 1.0"}
    params: Dict[str, Any] = {"archived": False, 'area': 113, 'per_page': 100}

    def get_vacancies(self, keyword: Optional[str] = None) -> List[Vacancy]:
        """
        The get_vacancies function overrides the base class abstract method. It accepts its own instance
        and a keyword as a string as parameters. It contains the necessary settings and, when called,
        makes an API request to the HeadHunter service, receives the result of the request,
        converts the response into a list of instances of the Vacancy class, and returns it.
        """
        if keyword is not None:
            self.params["text"] = keyword

        response = requests.get(self.base_url, headers=self.headers, params=self.params).json()['items']

        vacancies: list = []

        for item in response:
            result: dict = {}
            result["name"] = item.get('name')
            result["url"] = item.get('alternate_url')
            result["employer"] = item.get('employer').get('name')
            if item["salary"] is not None:
                result["salary_from"] = item['salary'].get('from') if item['salary'].get('from') is not None else 0
                result["salary_to"] = item['salary'].get('to')if item['salary'].get('to') is not None else 0
            else:
                result["salary_from"] = 0
                result["salary_to"] = 0
            result["description"] = item["snippet"].get('requirement', None)

            vacancies.append(result)

        return dict_to_instance(vacancies)


# Code to check if the class is functioning correctly
if __name__ == '__main__':
    from views.view import display_vacancies

    hh = HeadHunterParser()
    vac = hh.get_vacancies('Python')
    display_vacancies(vac)