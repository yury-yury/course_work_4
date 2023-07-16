from typing import List
import pandas

from functions import dict_to_instance, create_dict_for_data_frame_pandas
from vacancies.vacancy import Vacancy
from views.savers.abstract_saver import AbstractSaver


class ExelSaver(AbstractSaver):
    """
    The ExelSaver class is designed to provide an application with a file in the exel format.
    Inherited from the abstract base class AbstractSaver.
    """
    file_path: str = './exel_data.xlsx'

    def write_data(self, data: List[Vacancy]) -> None:
        """
        The write_data function overrides the base class abstract method. It takes as parameters
        an instance of its own class and data to write as a list of Vacancy class instances.
        Transforms the passed data into a pandas DataFrame object and writes the data to an exel file,
        the path to which is specified in the class arguments.
        """
        data.sort(key=lambda x: x.salary_from, reverse=True)
        data_frame = pandas.DataFrame(create_dict_for_data_frame_pandas(data))
        data_frame.to_excel(self.file_path, index=False)

    def get_data(self) -> List[Vacancy]:
        """
        The get_data function overrides the base class abstract method. It takes as a parameter an instance
        of its own class. It reads all the data from the exel file, the path to which is defined
        in the class arguments, and converts the received data into a list of instances of the Vacancy class.
        Returns the generated list.
        """
        excel_data_frame = pandas.read_excel(self.file_path, sheet_name='Sheet1')
        return dict_to_instance(excel_data_frame.to_dict(orient='records'))


# Code to check if the class is functioning correctly
if __name__ == '__main__':
    from parser.head_hunter.head_hunter_parser import HeadHunterParser

    hh = HeadHunterParser()
    data = hh.get_vacancies()

    saver = ExelSaver()
    saver.write_data(data)
    saver.delete_data()
