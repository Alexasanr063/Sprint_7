import requests
from Sprint_7.data import Accept_Order

class TestCourierRegistration:
    """Тесты регистрации курьера"""

    def test_get_courier_orders(self):
        """Получение заказов курьера"""
        response = requests.get(Accept_Order.list_of_orders)
        assert response.status_code == 200
        assert 'orders' in response.json()