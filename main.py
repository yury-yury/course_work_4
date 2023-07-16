from typing import Optional, List, Tuple

from parser.abstract_parser import AbstractParser
from parser.head_hunter.head_hunter_parser import HeadHunterParser
from parser.super_job.super_job_parser import SuperJobParser
from views.savers.json_saver import JsonSaver
from views.view import display_vacancies


def main():
    """
    The main function represents a function for interacting with the user through the console.
    Creates class instances. Binds the functioning of the program into a single shell.
    """
    saver = JsonSaver()
    parsers: List[Tuple[str, AbstractParser]] = [('HeadHunter', HeadHunterParser()), ('SuperJob', SuperJobParser())]

    print('Welcome dear user!')
    while True:
        print()
        print('Shall we continue? Type cancel to exit the program.')
        if input(': ').strip().lower() == 'cancel':
            break
        data: list = []
        print('Jobs with what keyword will we search for? To search all vacancies, press enter.')
        keyword: Optional[str] = input(': ').strip().lower()
        if keyword == '' or keyword == ' ':
            keyword = None

        for item in parsers:
            print()
            print(f'Do a search on the {item[0]} platform? Enter yes or no.')
            if input(': ').strip().lower() == 'yes':
                parser = item[1]
                data += parser.get_vacancies(keyword)

        if data == []:
            print('Data for further use has not been received.')
            continue
        else:
            saver.write_data(data)
            print(f'Found {len(data)} vacancies.')
        print()
        print('Enter the number of vacancies to display.')
        count = int(input(': '))
        _data = saver.get_data()
        display_vacancies(_data[:count])


if __name__ == '__main__':
    main()