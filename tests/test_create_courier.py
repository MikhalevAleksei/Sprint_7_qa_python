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

    @allure.step('Check courier created')
    def test_create_courier(self):
        assert len(gen_data()) > 0

    @allure.step('Check no same courier')
    def test_no_same_courier(self):
        response = requests.post(
            f"{Urls.HOME_URL}{Handlers.CREATE_COURIER}",
            data=TestCreateCourier.data)
        assert response.status_code == 409, "Courier created with same data"

    @pytest.mark.parametrize('login, password, firstName',
                        [
                            ('', gen_data()[1], gen_data()[2]),
                            (gen_data()[0], '', gen_data()[2]),
                            (gen_data()[0], gen_data()[1], ''),
                            ('', '', '')
                        ]
                        )
    @allure.step('Check authorisation with not all date')
    def test_authorisation_with_not_all_date(self, login, password, firstName):
        negative_auth_data = {'login': login, 'password': password,
                              'firstName': firstName}

        response = requests.post(f"{Urls.HOME_URL}{Handlers.CREATE_COURIER}", \
                                 data=negative_auth_data)
        assert response.status_code == 400, "Courier created with not all data"

    @allure.step('Check status code')
    def test_status_code(self):
        response = requests.post(f"{Urls.HOME_URL}{Handlers.CREATE_COURIER}",
                                 data=TestCreateCourier.data)
        assert response.status_code == 201, "Courier not created. Status " \
                                            "code wrong"

    @allure.step('Check response body')
    def test_response_body(self):
        response = requests.post(f"{Urls.HOME_URL}{Handlers.CREATE_COURIER}", \
                                 data=TestCreateCourier.data)
        assert response.json()['ok'] == 'true'

    @pytest.mark.parametrize('login, password, firstName',
                        [
                            ('', gen_data()[1], gen_data()[2]),
                            (gen_data()[0], '', gen_data()[2]),
                            (gen_data()[0], gen_data()[1], '')
                        ]
                        )
    @allure.step('Check authorisation error message')
    def test_authorisation_with_not_all_date(self, login, password, firstName):
        negative_auth_data = {'login': login, 'password': password,
                              'firstName': firstName}

        response = requests.post(f"{Urls.HOME_URL}{Handlers.CREATE_COURIER}", \
                                 data=negative_auth_data)
        assert response.json()[1] == 'message": "Недостаточно данных для ' \
                                      'создания учетной записи', "Wrong " \
                                                                 "message"

    @allure.step('Check message for creating courier with same login')
    def test_message_for_same_courier_login(self):
        response = requests.post(
            f"{Urls.HOME_URL}{Handlers.CREATE_COURIER}",
            data=TestCreateCourier.data)
        assert response.json()['message'] == 'Этот логин уже используется', \
            "Message for the same login is wrong"

    @classmethod
    def teardown_class(cls):
        cls.data.clear()


