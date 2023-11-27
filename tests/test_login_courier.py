import allure
import pytest
import requests

from generator import register_new_courier_and_return_login_password as \
    gen_data
from urls import Urls
from handlers import Handlers


class TestLoginCourier:
    data = {}

    @classmethod
    def setup_class(cls):
        cls.data["login"] = gen_data()[0]
        cls.data["password"] = gen_data()[1]
        cls.data["firstName"] = gen_data()[2]

    @allure.step('Check courier authorisation')
    def test_courier_authorisation(self):
        pass

    @allure.step('Check you need all data for authorisation')
    def test_need_all_data_for_authorisation(self):
        pass

    @allure.step('Check_error_message_if_wrong_login_or_password')
    def test_return_error_message_for_negative_login(self):
        pass

    @allure.step('Check_error_message_if_not_all_data')
    def test_error_message_not_all_data(self):
        pass

    @allure.step('Check_error_message_if_user_have_not_registration')
    def test_return_error_for_unknown_user(self):
        pass

   @allure.step('Check_success_login_return_id')
   def test_return_id_for_login():
    pass






    @classmethod
    def teardown_class(cls):
        cls.data.clear()
