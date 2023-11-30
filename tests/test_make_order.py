import allure
import requests

from generator import make_new_order_and_return_data
from handlers import Handlers
from urls import Urls


class TestMakeOrder:
    data = []

    @classmethod
    def setup_class(cls):
        order = make_new_order_and_return_data()
        cls.data.append(order)

    @allure.title('Check can choose black color for scooter')
    def test_choose_black_color(self, scooter_with_color_order):
        response = requests.post(
            f'{Urls.HOME_URL}{Handlers.MAKE_ORDER}',
            data=scooter_with_color_order(['BLACK']))
        assert response.status_code == 201

    @allure.title('Check can choose grey color for scooter')
    def test_choose_grey_color(self, scooter_with_color_order):
        response = requests.post(
            f'{Urls.HOME_URL}{Handlers.MAKE_ORDER}',
            data=scooter_with_color_order(['GREY']))
        assert response.status_code == 201

    @allure.title('Check can use both colors for scooter')
    def test_choose_both_colors(self, scooter_with_color_order):
        response = requests.post(
            f'{Urls.HOME_URL}{Handlers.MAKE_ORDER}',
            data=scooter_with_color_order(['BLACK', 'GREY']))
        assert response.status_code == 201

    @allure.title('Check order scooter without color')
    def test_order_without_scooter_color(self, without_color_scooter_order):
        response = requests.post(
            f'{Urls.HOME_URL}{Handlers.MAKE_ORDER}',
            data=without_color_scooter_order)
        assert response.status_code == 201

    @allure.title('Check answer body has track')
    def test_order_response_has_track(self, without_color_scooter_order):
        response = requests.post(
            f'{Urls.HOME_URL}{Handlers.MAKE_ORDER}',
            data=without_color_scooter_order)
        assert 'track' in response.json()

    @classmethod
    def teardown_class(cls):
        cls.data.clear()
