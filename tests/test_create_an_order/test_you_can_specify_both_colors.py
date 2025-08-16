import requests
from Sprint_7.data import Accept_Order,Data_For_The_Test
import pytest
class TestOrderCreation:
    """Тесты создания заказа"""
    @pytest.mark.parametrize("param",[Data_For_The_Test.payload,Data_For_The_Test.payload_1,Data_For_The_Test.payload_2,Data_For_The_Test.payload_3])
    def test_create_color_both(self,param):
        response = requests.post(Accept_Order.create_an_order_1, json=param)
        print(response.json())
        assert response.status_code == 201
        assert 'track' in response.json()
