"""
Cli report module works with CLI
For example:

python cli_report.py --files <folder_path> [--asc | --desc]  shows list of drivers and optional order (default order is asc)
python cli_report.py --files <folder_path> --driver “Sebastian Vettel”  shows statistic about driver
"""
import argparse
from prettytable import PrettyTable

from report import sort_race_logs, main as main_report


def parse_args() -> argparse:
    """
    Parse cli arguments with argparse
    :param:
    :return instance of argparse:
    """
    parser = argparse.ArgumentParser(prog='CLI Interface to report framework',
                                     usage='%(prog)s cli_report.py \"[--files "<folder_path>" [--asc | --desc] --driver]"',
                                     description='Show report about racing logs')
    parser.add_argument('--files',
                        type=str,
                        help='path to folder with txt files',
                        required=True)
    parser.add_argument('--asc',
                        action='store_true',
                        help='order by ascending',
                        default=False,
                        required=False)
    parser.add_argument('--desc',
                        action='store_true',
                        help='order by descending',
                        default=False,
                        required=False)
    parser.add_argument('--driver',
                        type=str,
                        help='shows statistic about driver',
                        default=None,
                        required=False)
    args = parser.parse_args()
    return args


def print_race_result_table(race_results: dict[str], abbrs: dict[str: tuple[str]], current_driver: str):
    """Print console table with race results"""
    race_limit = 15
    found_driver = False
    cli_table = PrettyTable()
    cli_table.field_names = ["№", "Driver", "Company", "Race time"]
    for counter, code in enumerate(race_results):
        driver = abbrs[code][0]
        company = abbrs[code][1]
        race_time = race_results[code]
        if current_driver:
            if driver == current_driver:
                cli_table.add_row([counter + 1, driver, company, race_time])
                found_driver = True
                break
            continue
        cli_table.add_row([counter + 1, driver, company, race_time])
        if counter + 1 == race_limit:
            cli_table.add_row(['#' * 2, '#' * 18, '#' * 20, '#' * 16])
    if current_driver and not found_driver:
        print('Driver not found')
        return -1
    print(cli_table)


def main(folder: str | None, order_asc: bool, order_desc: bool, driver: str | None):
    """Main controller of cli_report module"""
    if order_asc and order_desc:
        print('Cannot use two options together: --asc --desc')
        return False
    try:
        race_results, abbrs = main_report(folder)
    except FileNotFoundError as e:
        print(e)
        return False
    race_results_sorted = sort_race_logs(race_results, order_desc)
    print_race_result_table(race_results_sorted, abbrs, driver)


if __name__ == '__main__':
    args = parse_args()
    folder = args.files
    order_asc = args.asc
    order_desc = args.desc
    driver = args.driver
    main(folder, order_asc, order_desc, driver)
