import requests

from faker import Faker

from handlers import Handlers
from urls import Urls

fake = Faker(locale="ru_RU")


def fake_user_registration():
    fake_data = []
    fake_login = fake.email()
    fake_password = fake.password()
    fake_firstName = fake.first_name()

    fake_data.append(fake_login)
    fake_data.append(fake_password)
    fake_data.append(fake_firstName)
    return fake_data




