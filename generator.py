from datetime import datetime
from random import randint

import requests

from handlers import Handlers
from helpers import generate_random_string, fake_make_order, fake
from urls import Urls


def register_new_courier_and_return_login_password():
    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = \
        requests.post(
            f'{Urls.HOME_URL}{Handlers.CREATE_COURIER}',
            data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


def make_new_order_and_return_data():
    order_data = []
    fake_firstName = fake.first_name()
    fake_lastName = fake.last_name()
    fake_address = fake.address()
    ran_metroStation = randint(1, 10)
    fake_phone = fake.phone_number()
    ran_rentTime = randint(1, 5)
    deliveryDate = datetime.now()
    fake_comment = generate_random_string(9)

    payload = {
        "firstName": fake_firstName,
        "lastName": fake_lastName,
        "address": fake_address,
        "metroStation": ran_metroStation,
        "phone": fake_phone,
        "rentTime": ran_rentTime,
        "deliveryDate": deliveryDate,
        "comment": fake_comment
    }
    response = \
        requests.post(
            f'{Urls.HOME_URL}{Handlers.MAKE_ORDER}',
            data=payload)

    if response.status_code == 201:
        order = fake_make_order()
        order_data.append(order)

    return order_data


def create_courier():
    created_courier = register_new_courier_and_return_login_password()
    return created_courier
