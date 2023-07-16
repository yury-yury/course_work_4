from abc import ABCMeta, abstractmethod
from typing import Optional


class AbstractParser(metaclass=ABCMeta):
    """
    The AbstractParser class is an abstract class. Inherited from class ABC from module abc.
    Defines methods that must be overridden in inherited classes.
    """
    @abstractmethod
    def get_vacancies(self, keyword: Optional[str]):
        """
        The get_vacancies function defines an abstract class method that must be overridden in a child class.
        """
        pass