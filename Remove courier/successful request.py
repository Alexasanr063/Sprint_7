import requests
import random
import string

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def test_remove_courier():


    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier/585595')

    # возвращаем список
    print(response.json())
    assert response.status_code == 200
