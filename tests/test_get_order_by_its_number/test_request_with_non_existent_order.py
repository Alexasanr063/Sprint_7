import requests
from Sprint_7.data import Accept_Order,Text_Of_Mistake

class TestOrderAcceptance:
    """Тесты принятия заказов"""

    def test_order_not_found(self):
        """Проверка ошибки при несуществующем заказе"""
        response = requests.get(Accept_Order.order_not_found_1)
        assert response.json()['message'] == Text_Of_Mistake.errer_5

    def test_missing_track_number(self):
        """Проверка ошибки при отсутствии номера заказа"""
        response = requests.get(Accept_Order.order_not_found_2)
        assert response.json()['message'] == Text_Of_Mistake.errer_3

    def test_successful_order_tracking(self):
        """Проверка успешного получения заказа"""
        response = requests.get(Accept_Order.order_not_found_3)
        assert 'order' in response.json()

