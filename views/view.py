from typing import List
import pandas

from functions import create_dict_for_data_frame_pandas
from vacancies.vacancy import Vacancy


def display_vacancies(data: List[Vacancy]) -> None:
    """
    The display_vacancies function takes as an argument a list of instances of the Vacancy class.
    Produces the output of the received data in a comfortable form using the tools of the pandas library.
    """
    pandas.set_option('display.max_row', None)
    pandas.set_option('display.max_columns', None)
    pandas.options.display.expand_frame_repr = False

    num_row: int = len(data)
    data_frame = pandas.DataFrame(create_dict_for_data_frame_pandas(data))
    print(data_frame.head(num_row))
    print('-' * 120)
