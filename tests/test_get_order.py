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

    @allure.step('Check success get order response get order has {"ok":true}')
    def test_get_order_response_has_ok_true(self):
        pass

    @allure.step('Check get order request without id return error')
    def test_negative_get_order_request_without_id(self):
        pass

    @allure.step('Check get order request with wrong id return error')
    def test_negative_id_get_order_request(self):
        pass

    @allure.step('Check get order request without order number return error')
    def test_negative_without_order_number_get_order_request(self):
        pass

    @allure.step('Check get order request with wrong order number return '
                 'error')
    def test_negative_order_number_get_order_request(self):
        pass

    @classmethod
    def teardown_class(cls):
        cls.data.clear()
