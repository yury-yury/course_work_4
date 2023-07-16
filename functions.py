from dataclasses import asdict
from typing import List, Dict, Any
import marshmallow
import marshmallow_dataclass

from vacancies.vacancy import Vacancy


def dict_to_instance(data: List[Dict[str, Any]]) -> List[Vacancy]:
    """
    The dict_to_instance function is a helper function. It takes as an argument a list of dictionaries
    with data to create instances of the Vacancy class. Performs data validation and creation of instances
    of the Vacancy class. If a data validation error is received, the instance being created is skipped.
    Returns the created list of instances of the Vacancy class.
    """
    result: list = []
    VacancySchema = marshmallow_dataclass.class_schema(Vacancy)

    for item in data:
        try:
            result.append(VacancySchema().load(item))
        except marshmallow.exceptions.ValidationError:
            continue
    return result


def instance_to_dict(data: List[Vacancy]) -> List[Dict[str, Any]]:
    """
    The instance_to_dict function is a helper function. It takes as an argument a list of instances
    of the Vacancy class. Produces the creation of dictionaries with data.
    Returns the generated list of dictionaries with data.
    """
    result: list = []
    for item in data:
        result.append(asdict(item))
    return result


def create_dict_for_data_frame_pandas(data: List[Vacancy]) -> Dict[str, list]:
    """
    The create_dict_for_data_frame_pandas function is a helper function. It takes as an argument
    a list of instances of the Vacancy class. Creates a data dictionary to create a DataFrame object
    from the pandas library. Returns the created data dictionary.
    """
    new_data: dict = {"name": [],
                       "url": [],
                       "employer": [],
                       "salary_from": [],
                       "salary_to": [],
                       "description": []}
    for item in data:
        new_data["name"].append(item.name)
        new_data["url"].append(item.url)
        new_data["employer"].append(item.employer)
        new_data["salary_from"].append(item.salary_from)
        new_data["salary_to"].append(item.salary_to)
        new_data["description"].append(item.description)

    return new_data
