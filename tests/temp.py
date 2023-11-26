import requests

from handlers import CREATE_COURIER
from generator import register_new_courier_and_return_login_password as paylot
from urls import HOME_URL


response = requests.post(f"{HOME_URL}{CREATE_COURIER}", data=paylot())
assert response.status_code == 201
