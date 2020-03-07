import re
import datetime
import requests

BIRTHDAY_PATTERN = re.compile("\\d{1,2}\\.\\d{1,2}\\.\\d{4}")
CURRENT_YEAR = datetime.datetime.today().year
BIRTHDAY_KEY = 'bdate'

ACCESS_TOKEN = '0d2d3d9f0d2d3d9f0d2d3d9f950d5d28d400d2d0d2d3d9f53729d867bd8486215092293'
VK_VERSION = '5.71'

AUTH_PARAMS = {
    "access_token": ACCESS_TOKEN,
    "v": VK_VERSION,
}


def _get_user_request(uid):
    params = {
        "user_ids": uid
    }
    params.update(AUTH_PARAMS)
    return requests.get("https://api.vk.com/method/users.get", params=params).json()


def _get_friends_request(user_id):
    params = {
        "user_id": user_id,
        "fields": BIRTHDAY_KEY,
    }
    params.update(AUTH_PARAMS)
    return requests.get("https://api.vk.com/method/friends.get", params=params).json()


def _get_users_friends(uid):
    users = _get_user_request(uid)
    user_id = users['response'][0].get('id', '')
    users_friends = _get_friends_request(user_id)
    return users_friends


def _filter_birthday_years(friends):
    birthday_years = []
    for friend in friends['response']['items']:
        birthday = friend.get(BIRTHDAY_KEY, '')
        birthday_match = BIRTHDAY_PATTERN.match(birthday)
        if birthday_match:
            year = birthday_match.group(0).split('.')[-1]
            birthday_years.append(year)
    return birthday_years


def calc_age(uid):
    users_friends = _get_users_friends(uid)
    birthday_years = _filter_birthday_years(users_friends)
    ages = [CURRENT_YEAR - int(year) for year in birthday_years]
    result = []
    for age in ages:
        pair = (age, ages.count(age))
        if pair not in result:
            result.append(pair)
    result.sort(key=lambda tup: (-tup[1], tup[0]))
    return result


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
