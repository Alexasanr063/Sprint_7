import requests
import random
import string

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def test_register_new_courier_and_return_login_password():

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId=585593')

    assert response.status_code == 200
    assert 'orders' in response.json()
