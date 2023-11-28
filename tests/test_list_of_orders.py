import allure
import pytest
import requests

from generator import register_new_courier_and_return_login_password as \
    gen_data
from urls import Urls
from handlers import Handlers


class TestCreateCourier:
    data = {}

    @classmethod
    def setup_class(cls):
        cls.data["login"] = gen_data()[0]
        cls.data["password"] = gen_data()[1]
        cls.data["firstName"] = gen_data()[2]

    @allure.step('Check response has list of orders')
    def test_response_has_list_orders(self):
        pass


    @classmethod
    def teardown_class(cls):
        cls.data.clear()
