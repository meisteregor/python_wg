import requests
import pprint
import urllib.request
import sys

APP_ID = '1c4256059e72d98d176c6cc47441914c'
BASE_URL = 'https://api.worldoftanks.ru/wot/account/'
LURL = BASE_URL + 'list/'
IURL = BASE_URL + 'info/'
TURL = BASE_URL + 'tanks/'
VURL = BASE_URL.replace('account/', 'encyclopedia/vehicles/')
IMG = "fav_tank_img.jpg"


def get_player_id(name):
    params = (('application_id', APP_ID), ('search', name), ('type', 'exact'))
    response = requests.get(LURL, params=params)
    try:
        player_data = response.json()['data'][0]['account_id']
        return player_data
    except (IndexError, KeyError):
        print("No such player found")
        sys.exit()


def find_in_nested_dict(d, key):
    for k, v in d.items():
        if k == key:
            return k, v
        else:
            if isinstance(v, list) and isinstance(v[0], dict):
                return_value = find_in_nested_dict(v[0], key)
                if return_value:
                    return return_value
            if isinstance(v, dict):
                return_value = find_in_nested_dict(v, key)
                if return_value:
                    return return_value


def get_player_favorite_tank_id(player_id_):
    params = (('application_id', APP_ID), ('account_id', player_id_))
    response = requests.get(TURL, params=params)
    player_tanks_all = response.json()
    player_favorite_tank_ = find_in_nested_dict(player_tanks_all, 'tank_id')
    return player_favorite_tank_[1]


def get_tank_info(tank_id):
    params = (
        ('application_id', APP_ID),
        ('tank_id', tank_id),

    )
    response = requests.get(VURL, params=params)
    return response.json()


def get_image_link(tank_id):
    params = (
        ('application_id', APP_ID),
        ('tank_id', tank_id),
        ('fields', 'images.big_icon'),
    )
    response = requests.get(VURL, params=params)
    data = response.json()
    image_link_ = find_in_nested_dict(data, 'big_icon')
    return image_link_[1]


def save_image(url, file):
    urllib.request.urlretrieve(url, file)


if __name__ == '__main__':
    player_nickname = input("Search player: ")
    player_id = get_player_id(player_nickname)
    player_favorite_tank_id = get_player_favorite_tank_id(player_id)
    print("{}'s favorite tanks full info:\n".format(player_nickname))
    tank_info = get_tank_info(player_favorite_tank_id)
    pprint.pprint(tank_info)
    image_link = get_image_link(player_favorite_tank_id)
    save_image(image_link, IMG)
