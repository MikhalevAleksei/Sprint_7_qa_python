from datetime import datetime
from random import randint

import pytest

from helpers import fake, generate_random_string


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

    return payload


@pytest.fixture(scope='function')
def scooter_with_color_order(without_color_scooter_order, color):
    scooter_payload = without_color_scooter_order()
    scooter_payload["color"] = color

    return scooter_payload
