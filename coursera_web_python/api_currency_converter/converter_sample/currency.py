from bs4 import BeautifulSoup
from decimal import Decimal

# import requests

CROSS_CUR = 'RUR'


def _parse_xml(soup, currency):
    try:
        char_code = soup.find('CharCode', text=currency)
        cur_exchange = char_code.find_next_sibling('Value').text.replace(',', '.')
        nominal = char_code.find_next_sibling('Nominal').text
        one_rur_cost = Decimal(nominal) / Decimal(cur_exchange)
    except AttributeError:
        print('Currency "{}" was not found during bank request!'.format(currency))
        char_code = cur_exchange = nominal = one_rur_cost = ''
    return char_code, cur_exchange, nominal, one_rur_cost


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp?date_req={}'.format(date))
    soup = BeautifulSoup(markup=response.content, features='xml')

    char_code_from, cur_exchange_from, nominal_from, one_rur_cost_from = _parse_xml(soup, cur_from)
    char_code_to, cur_exchange_to, nominal_to, one_rur_cost_to = _parse_xml(soup, cur_to)

    amount = Decimal(amount)

    result = amount
    if cur_from != CROSS_CUR and cur_to != CROSS_CUR:
        result = (one_rur_cost_to / one_rur_cost_from) * amount
    elif cur_from == CROSS_CUR and cur_to != CROSS_CUR:
        result = (one_rur_cost_to * amount)
    elif cur_from != CROSS_CUR and cur_to == CROSS_CUR:
        result = amount / one_rur_cost_from

    return result.quantize(Decimal('1.0000'))
