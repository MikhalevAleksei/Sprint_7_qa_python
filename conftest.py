from datetime import datetime
from random import randint

import pytest
import requests

from handlers import Handlers
from helpers import fake, generate_random_string
from urls import Urls


@pytest.fixture(scope='function')
def black_color_scooter_order():
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
        "comment": fake_comment,
        "color": ["BLACK"]

    }
    response = requests.post(
        f'{Urls.HOME_URL}{Handlers.MAKE_ORDER}', data=payload)

    return response


@pytest.fixture(scope='function')
def grey_color_scooter_order():
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
        "comment": fake_comment,
        "color": ["GREY"]

    }
    response = requests.post(
        f'{Urls.HOME_URL}{Handlers.MAKE_ORDER}', data=payload)

    return response


@pytest.fixture(scope='function')
def black_and_grey_color_scooter_order():
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
        "comment": fake_comment,
        "color": ["BLACK", "GREY"]

    }
    response = requests.post(
        f'{Urls.HOME_URL}{Handlers.MAKE_ORDER}', data=payload)

    return response


@pytest.fixture(scope='function')
def without_color_scooter_order():
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
        "comment": fake_comment,
    }
    response = requests.post(
        f'{Urls.HOME_URL}{Handlers.MAKE_ORDER}', data=payload)

    return response
