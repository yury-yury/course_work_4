from dataclasses import dataclass
from typing import Optional


@dataclass
class Vacancy:
    """
    The Vacancy class is a dataclass and represents a data model for use in an application.
    Contains the annotation of all fields and overridden "magic" methods.
    """
    name: str
    url: str
    employer: str
    salary_from: Optional[int]
    salary_to: Optional[int]
    description: Optional[str]

    def __repr__(self) -> str:
        """
        The __repr__ function overrides the magic method defined by the dataclass.
        Returns a string representation of the class instance.
        """
        return self.name

    def __lt__(self, other) -> bool:
        """
        The __lt__ function defines a magic method for comparing two instances of a class. It takes as parameters
        its own instance and another object to compare against. Defines the field by the value of which
        the comparison is made. Returns the boolean value of the result of comparing instances of the class.
        """
        return self.salary_from < other.salary_from

    def __le__(self, other) -> bool:
        """
        The __le__ function defines a magic method for comparing two instances of a class. It takes as parameters
        its own instance and another object to compare against. Defines the field by the value of which
        the comparison is made. Returns the boolean value of the result of comparing instances of the class.
        """
        return self.salary_from <= other.salary_from

    def __gt__(self, other) -> bool:
        """
        The __gt__ function defines a magic method for comparing two instances of a class. It takes as parameters
        its own instance and another object to compare against. Defines the field by the value of which
        the comparison is made. Returns the boolean value of the result of comparing instances of the class.
        """
        return self.salary_from > other.salary_from

    def __ge__(self, other) -> bool:
        """
        The __ge__ function defines a magic method for comparing two instances of a class. It takes as parameters
        its own instance and another object to compare against. Defines the field by the value of which
        the comparison is made. Returns the boolean value of the result of comparing instances of the class.
        """
        return self.salary_from >= other.salary_from

    def __eq__(self, other) -> bool:
        """
        The __eq__ function defines a magic method for comparing two instances of a class. It takes as parameters
        its own instance and another object to compare against. Defines the field by the value of which
        the comparison is made. Returns the boolean value of the result of comparing instances of the class.
        """
        return self.salary_from == other.salary_from
