import os
from pprint import pprint
from typing import Dict, Optional, List
import requests
from dotenv import load_dotenv

from functions import dict_to_instance
from parser.abstract_parser import AbstractParser
from vacancies.vacancy import Vacancy


load_dotenv()


class SuperJobParser(AbstractParser):
    """
    The SuperJobParser class inherits from the AbstractParser abstract class. Designed to request the
    SuperJob service API and get vacancies.
    """
    headers: Dict[str, str] = {'X-Api-App-Id': os.environ.get("SUPER_JOB_TOKEN")}
    base_url: str = 'https://api.superjob.ru/2.0/vacancies/'
    params = {"count": 100, "page": 0, "archive": False}

    def get_vacancies(self, keyword: Optional[str] = None) -> List[Vacancy]:
        """
        The get_vacancies function overrides the base class abstract method. It accepts its own instance
        and a keyword as a string as parameters. It contains the necessary settings and, when called,
        makes an API request to the HeadHunter service, receives the result of the request,
        converts the response into a list of instances of the Vacancy class, and returns it.
        """
        if keyword is not None:
            self.params["keyword"] = keyword
        response = requests.get(self.base_url, headers=self.headers, params=self.params).json()['objects']

        vacancies: list = list()

        for item in response:
            result: dict = {}
            result["name"] = item.get('profession')
            result["url"] = item.get('link')
            result["employer"] = item.get('client').get('title', 'Unknown')
            result["salary_from"] = item.get('payment_from', None)
            result["salary_to"] = item.get('payment_to', None)
            result["description"] = item.get('candidat', None)

            vacancies.append(result)

        return dict_to_instance(vacancies)

# Code to check if the class is functioning correctly
if __name__ == '__main__':
    from views.view import display_vacancies

    sj = SuperJobParser()
    vac = sj.get_vacancies('Python')
    display_vacancies(vac)