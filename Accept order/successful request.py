import requests
import random
import string

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def test_accept_order():
    get_id_response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=343249')
    id = get_id_response.json()['order']['id']

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{id}?courierId=585596')

    assert response.json() == {"ok":True}
