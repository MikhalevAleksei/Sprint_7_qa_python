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

    @allure.step('Check unsuccess deliting of courier return error')
    def test_negativ_del_courier_return_error(self):
        pass

    @allure.step('Check success response has {"ok":true}')
    def test_response_has_ok_true(self):
        pass

    @allure.step('Check request without id return error')
    def test_negative_request_without_id(self):
        pass

    @allure.step('Check request with wrong id return error')
    def test_negative_id_request(self):
        pass

    @allure.step('Check request without order number return error')
    def test_negative_without_order_number_request(self):
        pass

    @allure.step('Check request with wrong order number return error')
    def test_negative_order_number_request(self):
        pass


    @classmethod
    def teardown_class(cls):
        cls.data.clear()
