from abc import ABCMeta, abstractmethod
from typing import List, Optional

from vacancies.vacancy import Vacancy


class AbstractSaver(metaclass=ABCMeta):
    """
    The AbstractSaver class is an abstract base class intended to be further inherited by classes intended
    to work with external classes. Inherited from class ABC from module abc. Contains abstract methods
    for further mandatory redefinition in child classes, as well as methods that are general and independent
    of the type of files with which work is carried out.
    """
    file_path: str = ''

    @abstractmethod
    def write_data(self, data: List[Vacancy]) -> None:
        """
        The write_data function defines an abstract class method that must be overridden in a child class.
        It takes as parameters an instance of its own class and a list of data as a list
        of instances of the Vacancy class.
        """
        pass

    @abstractmethod
    def get_data(self) -> List[Vacancy]:
        """
        The get_data function defines an abstract class method that must be overridden in a child class.
        It takes an instance of its own class as a parameter.
        """
        pass

    def delete_data(self) -> None:
        """
        The delete_data function defines a class method to use its functionality in all child classes.
        It takes an instance of its own class as a parameter. Deletes the entire contents of the file specified
        in the class attributes of the child class.
        """
        open(self.file_path, 'w').close()

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        The add_vacancy function defines a class method to use its functionality in all child classes.
        It takes as parameters an instance of its own class and an instance of the Vacancy class.
        Retrieves data from a storage file, adds an instance of the Vacancy class to its contents,
        and writes the updated data to a file.
        """
        vacancies: List[Vacancy] = self.get_data()
        vacancies.append(vacancy)
        self.write_data(vacancies)

    def get_vacancies_by_salary(self, salary: str) -> List[Vacancy]:
        """
        The get_vacancies_by_salary function defines a base class method and is intended to be used in child classes.
        It takes as parameters an instance of its own class and a query in the form of a string.
        Parses request values, requests all data stored in the file, filters instances by the value
        of the salary_from field, returns instances of the Vacancy class that satisfy the request
        as a list of instances of the Vacancy class.
        """
        salary: List[str] = salary.split('-')
        for i in range(2):
            salary[i]: List[str] = salary[i].split()
            result: str = ''
            for j in range(len(salary[i])):
                if salary[i][j].isdigit():
                    result += salary[i][j]
            salary[i]: str = result

        vacancies = self.get_data()
        filtred_vacancies: List[Vacancy] = list(filter(
            lambda x: x.salary_from >= int(salary[0]) and x.salary_from <= int(salary[1]), vacancies
        ))
        return filtred_vacancies

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        The delete_vacancy function defines a class method to use its functionality in all child classes.
        It takes as parameters an instance of its own class and an instance of the Vacancy class.
        Retrieves data from a storage file, finds an instance of the Vacancy class corresponding to the one
        received in the arguments, removes it from the stored data, and writes the updated data to the file.
        """
        vacancies: List[Vacancy] = self.get_data()

        i_del: Optional[int] = None

        for i, instance in enumerate(vacancies):
            if instance.url == vacancy.url:
                i_del = i
                break

        if i_del is not None:
            vacancies.pop(i_del)

        self.write_data(vacancies)
