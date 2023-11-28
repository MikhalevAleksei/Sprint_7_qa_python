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

    @allure.step('Check success order request by number return order object')
    def test_positive_get_order_by_number(self):
        pass

    @allure.step('Check get order by number request without order number '
                 'return error')
    def test_negative_without_order_number_order_request(self):
        pass

    @allure.step('Check get order by number request with wrong order number '
                 'return error')
    def test_negative_order_number_order_request(self):
        pass


    @classmethod
    def teardown_class(cls):
        cls.data.clear()
