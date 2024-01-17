import os
from bs4 import BeautifulSoup

from utils.exporter import convert_to_json, remove_old_data, save_to_sqlite
from utils.parser import get_perforated_aluminum_sheet, get_perforated_stainless_steel_sheet
from utils.utils import check_reports_folder_exist, get_requests, print_template, random_sleep


os.environ['PROJECT_ROOT'] = os.path.dirname(os.path.abspath(__file__))


def start():
    try:
        reports_folder = check_reports_folder_exist()

        if not reports_folder:
            return False

        products = get_perforated_stainless_steel_sheet()
        products += get_perforated_aluminum_sheet()
        # save_to_sqlite(products_to_save, reports_folder)
    except Exception as ex:
        print_template(f'Error: {ex}')
        return False


if __name__ == '__main__':
    reports_folder = check_reports_folder_exist()
    if reports_folder:
        remove_old_data(reports_folder)

        start()

        total_count = convert_to_json(reports_folder)
        print(f"Total count: {total_count}")
