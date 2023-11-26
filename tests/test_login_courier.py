import requests

from handlers import Handlers
from generator import register_new_courier_and_return_login_password as paylot
from urls import Urls


class TestLoginCourier:

    def test_login_courier(self):
        response = requests.post(
            f"{Urls.HOME_URL}{Handlers.CREATE_COURIER}", data=paylot())
        print(paylot()[0])

