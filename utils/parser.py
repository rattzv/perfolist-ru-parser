

from bs4 import BeautifulSoup
from utils.utils import get_current_time, get_requests, print_template


def get_perforated_stainless_steel_sheet():
    url = 'https://www.perfolist.ru/produkt/perfolist/nerjaveyushiy/'
    response = get_requests(url)
    if response is False:
        return False

    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', 'default-table')

    if table is None:
        return False

    name = table.find('thead').get_text(separator=", ", strip=True)

    table_head = soup.find('tbody').find('tr')
    headers = [header.get_text(strip=True) for header in table_head.find_all('th')]

    rows = table.find('tbody').find_all('tr')[1:]

    products = []
    chapter = None
    category = None

    breadcrumbs = soup.find('ul', 'breadcrumbs')
    if breadcrumbs:
        breadcrumbs_items = breadcrumbs.find_all('li')
        if len(breadcrumbs_items) > 1:
            chapter = breadcrumbs_items[1].get_text(strip=True)
        if len(breadcrumbs_items) > 2:
            category = breadcrumbs_items[2].get_text(strip=True)

    for row in rows:
        columns = row.find_all('td')
        product_data = {}
        product_data['Наименование'] = name.replace('"', "'").replace('\xa0', ' ')
        product_data['URL товара'] = url
        if chapter:
            product_data['Раздел'] = chapter
        if category:
            product_data['Категория'] = category
        product_data['Время парсинга (мск)'] = get_current_time()

        for i, header in enumerate(headers):
            product_data[header.replace('"', "'").replace('\xa0', ' ')] = columns[i].get_text(strip=True).replace('"', "'").replace('\xa0', ' ')

        products.append(product_data)
    return products


def get_perforated_aluminum_sheet():
    url = 'https://www.perfolist.ru/produkt/perfolist/aluminiyeviy/'
    response = get_requests(url)
    if response is False:
        return False

    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', 'default-table')

    if table is None:
        return False

    name = table.find('thead').get_text(separator=", ", strip=True)

    table_head = soup.find('tbody').find('tr')
    headers = [header.get_text(strip=True) for header in table_head.find_all('th')]

    rows = table.find('tbody').find_all('tr')[1:]

    products = []
    chapter = None
    category = None

    breadcrumbs = soup.find('ul', 'breadcrumbs')
    if breadcrumbs:
        breadcrumbs_items = breadcrumbs.find_all('li')
        if len(breadcrumbs_items) > 1:
            chapter = breadcrumbs_items[1].get_text(strip=True)
        if len(breadcrumbs_items) > 2:
            category = breadcrumbs_items[2].get_text(strip=True)

    for row in rows:
        columns = row.find_all('td')
        product_data = {}
        product_data['Наименование'] = name.replace('"', "'").replace('\xa0', ' ')
        product_data['URL товара'] = url

        if chapter:
            product_data['Раздел'] = chapter
        if category:
            product_data['Категория'] = category
        product_data['Время парсинга (мск)'] = get_current_time()

        for i, header in enumerate(headers):
            last_column_count = len(columns)

            rowspan = columns[i].get('rowspan')
            if rowspan:
                print(rowspan)
                
            key = header.replace('"', "'").replace('\xa0', ' ')

            value = columns[i].get_text(strip=True).replace('"', "'").replace('\xa0', ' ')
            product_data[key] = value

        print(product_data)
        products.append(product_data)
    return products