import csv
from typing import List, Dict, Any

from functions import instance_to_dict, dict_to_instance
from vacancies.vacancy import Vacancy
from views.savers.abstract_saver import AbstractSaver


class CSVSaver(AbstractSaver):
    """
    The CSVSaver class is designed to provide an application with a file in the csv format.
    Inherited from the abstract base class AbstractSaver.
    """
    file_path: str = './csv_data.csv'

    def write_data(self, data: List[Vacancy]) -> None:
        """
        The write_data function overrides the base class abstract method. It takes as parameters an instance
        of its own class and data to write as a list of Vacancy class instances.
        Converts the passed data into a list of dictionaries and writes the data to a csv file,
        the path to which is specified in the class arguments.
        """
        data.sort(key=lambda x: x.salary_from, reverse=True)
        vacancies: List[Dict[str, Any]] = instance_to_dict(data)

        with open(self.file_path, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=vacancies[0])
            writer.writeheader()
            writer.writerows(vacancies)


    def get_data(self) -> List[Vacancy]:
        """
        The get_data function overrides the base class abstract method. It takes as a parameter an instance
        of its own class. It reads all the data from the csv file, the path to which is defined
        in the class arguments, and converts the received data into a list of instances of the Vacancy class.
        Returns the generated list.
        """
        with open(self.file_path, encoding="utf8") as file:
            reader = csv.DictReader(file)
            vacancies: List[Dict[str, Any]] = []
            for row in reader:
                vacancies.append(row)
        return dict_to_instance(vacancies)


# Code to check if the class is functioning correctly
if __name__ == '__main__':
    from parser.head_hunter.head_hunter_parser import HeadHunterParser
    from views.view import display_vacancies

    hh = HeadHunterParser()
    data = hh.get_vacancies('Python разработчик')

    saver = CSVSaver()

    saver.write_data(data)
    display_vacancies(saver.get_data())
    vac = Vacancy(name="test", url="test", employer="test", salary_from=0, salary_to=None, description=None)
    saver.add_vacancy(vac)
    # display_vacancies(saver.get_data())
    saver.delete_vacancy(vac)
    # display_vacancies(saver.get_data())
    # display_vacancies(saver.get_vacancies_by_salary("150 000-200 000 руб."))
    saver.delete_data()
