from generator import register_new_courier_and_return_login_password


def test_create_courier():
    assert register_new_courier_and_return_login_password()
