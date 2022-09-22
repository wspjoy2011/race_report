"""
Report module of Monaco racing 2018
Shows list of drivers and optional order
Shows statistic about driver
"""
import os
import re
from datetime import datetime

from file_handler import read_data_fromfile
from get_base_dir import get_base_dir


def get_data_from_file(folder: str) -> tuple[list[str], list[str], list[str]]:
    """
    Get racing data from folder
    :param folder
    Folder name of racing monitor data:
    :return start_log, end_log, abbr_txt
    Return tuple of lists with data from files:
    """
    if not isinstance(folder, str):
        raise TypeError('Input data must be string!')

    base_dir = os.path.join(get_base_dir(), folder)
    path_to_start = os.path.join(base_dir, 'start.log')
    path_to_end = os.path.join(base_dir, 'end.log')
    path_to_abbr = os.path.join(base_dir, 'abbreviations.txt')

    start_log = sorted(read_data_fromfile(path_to_start))
    end_log = sorted(read_data_fromfile(path_to_end))
    abbr_txt = sorted(read_data_fromfile(path_to_abbr))

    return start_log, end_log, abbr_txt


def parse_data_from_log(data: list[str]) -> dict[dict[str]]:
    """Parse data from start.log and end.log"""
    racers = {}
    for race in data:
        racer_abbr = re.findall(r'^.{0,3}', race)[0]
        race_date = re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', race)[0]
        race_time = re.findall(r'[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}$', race)[0]
        if not all((racer_abbr, race_date, race_time)):
            raise ValueError('Wrong data in start.log | end.log')
        racers[racer_abbr] = f'{race_date} {race_time}'
    return racers


def parse_data_from_abbr(abbrs: list[str]) -> dict[tuple[str]]:
    """Parse data from abbreviations.txt"""
    abbrs_map = {}
    for line in abbrs:
        if len(line.split('_')) != 3:
            raise ValueError('Wrong data in abbreviations.txt')
        abbr, driver, company = line.split('_')
        abbrs_map[abbr] = driver, company
    return abbrs_map


def calc_results(start_data: dict[dict[str]], end_data: dict[dict[str]]) -> dict[str: datetime]:
    """Calc race results"""
    race_results = {}
    for racer, race_datetime in end_data.items():
        start_time = datetime.strptime(start_data[racer], "%Y-%m-%d %H:%M:%S.%f")
        end_time = datetime.strptime(race_datetime, "%Y-%m-%d %H:%M:%S.%f")
        race_result = end_time - start_time if end_time >= start_time else start_time - end_time
        race_results[racer] = str(race_result)
    return race_results


def sort_race_logs(race_log: dict[str: datetime], reverse: bool = False) -> dict[str: datetime]:
    """Sort log race dict by values(race time)"""
    return dict(sorted(race_log.items(), key=lambda item: item[1], reverse=reverse))


def main(folder: str):
    """Main controller"""
    start_log, end_log, abbr_txt = get_data_from_file(folder)
    start_data = parse_data_from_log(start_log)
    end_data = parse_data_from_log(end_log)
    abbr_data = parse_data_from_abbr(abbr_txt)
    race_results = calc_results(start_data, end_data)
    return race_results, abbr_data

