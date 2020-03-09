from bs4 import BeautifulSoup
from decimal import Decimal

import requests


def _process_amount(amount):
    pass


def convert(amount, cur_from, cur_to, date, requestss):
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp?date_req={}'.format(date))
    soup = BeautifulSoup(markup=response.content, features='xml')

    char_code_from = soup.find('CharCode', text=cur_from)
    cur_from_exchange = char_code_from.find_next_sibling('Value').text.replace(',', '.')
    nominal_from = char_code_from.find_next_sibling('Nominal').text
    one_rur_exchange_cur_from = (Decimal(cur_from_exchange) / Decimal(nominal_from)).quantize(Decimal('1.0000'))

    char_code_to = soup.find('CharCode', text=cur_to)
    cur_to_exchange = char_code_to.find_next_sibling('Value').text.replace(',', '.')
    nominal_to = char_code_to.find_next_sibling('Nominal').text
    one_rur_exchange_cur_to = (Decimal(cur_to_exchange) / Decimal(nominal_to)).quantize(Decimal('1.0000'))

    result = (one_rur_exchange_cur_from / one_rur_exchange_cur_to * Decimal(amount)).quantize(Decimal('1.0000'))

    return result


print(convert('1000.1000', 'AMD', 'JPY', '07/03/2020', ''))
