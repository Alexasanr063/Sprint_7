import requests
import random
import string


def test_accept_order():

    response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=343249')

    assert 'order' in response.json()
