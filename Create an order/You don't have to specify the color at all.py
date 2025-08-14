import requests
import random
import string

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def test_create_not_color():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки


    # собираем тело запроса
    payload = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha"
}

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=payload)

    print(response.json())
    assert response.status_code ==201
    assert 'track' in response.json()

