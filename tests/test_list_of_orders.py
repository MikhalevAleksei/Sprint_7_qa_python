import allure
import pytest
import requests

from generator import make_new_order_and_return_data
from urls import Urls
from handlers import Handlers


class TestCreateCourier:
    data = {}

    @classmethod
    def setup_class(cls):
        order = make_new_order_and_return_data()
        cls.data.append(order)

    @allure.step('Check response has list of orders')
    def test_response_has_list_orders(self):
        response = requests.get(f'{Urls.HOME_URL}{Handlers.MAKE_ORDER}')
        assert len(response.json()) > 0

    @classmethod
    def teardown_class(cls):
        cls.data.clear()
