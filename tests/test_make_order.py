import allure

from generator import make_new_order_and_return_data


class TestMakeOrder:
    data = []

    @classmethod
    def setup_class(cls):
        order = make_new_order_and_return_data()
        cls.data.append(order)

    @allure.step('Check can choose black color for scooter')
    def test_choose_black_color(self, black_color_scooter_order):
        assert black_color_scooter_order.status_code == 201

    @allure.step('Check can choose grey color for scooter')
    def test_choose_grey_color(self, grey_color_scooter_order):
        assert grey_color_scooter_order.status_code == 201

    @allure.step('Check can use both colors for scooter')
    def test_choose_both_colors(self, black_and_grey_color_scooter_order):
        assert black_and_grey_color_scooter_order.status_code == 201

    @allure.step('Check order scooter without color')
    def test_order_without_scooter_color(self, without_color_scooter_order):
        assert without_color_scooter_order.status_code == 201

    @allure.step('Check answer body has track')
    def test_body_has_track(self, without_color_scooter_order):
        assert 'track' in without_color_scooter_order.json()

    @classmethod
    def teardown_class(cls):
        cls.data.clear()
