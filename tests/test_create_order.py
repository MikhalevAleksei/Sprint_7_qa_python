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

    @allure.step('Check can choose two color black and grey')
    def test_choose_two_colors_black_or_grey(self):
        pass

    @allure.step('Check can use both colors')
    def test_choose_both_colors(self):
        pass

    @allure.step('Check order scooter without color')
    def test_order_without_scooter_color(self):
        pass

    @allure.step('Check answer body has track')
    def test_body_has_track(self):
        pass


    @classmethod
    def teardown_class(cls):
        cls.data.clear()
