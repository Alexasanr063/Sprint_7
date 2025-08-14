import requests
import random
import string

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def test_accept_order():

    response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=')

    assert response.json()['message'] == "Недостаточно данных для поиска"
