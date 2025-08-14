import requests
import random
import string

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def test_accept_order():

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.put('https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/145?courierId=585596')

    assert response.json()['message'] == 'Заказа с таким id не существует'
