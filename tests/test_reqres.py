from pytest_voluptuous import S
from schemas.schemas import *


def test_create_user(reqres):
    created_user = reqres.post("api/users", {"name": "Alex", "job": "Tester"})

    assert created_user.status_code == 201
    assert S(create_user) == created_user.json()
    assert created_user.json()["name"] == "Alex"
    assert created_user.json()["job"] == "Tester"


def test_update_user_by_put(reqres):
    update_user = reqres.put("api/users/2", {"name": "sant", "job": "aqa"})

    assert update_user.status_code == 200
    assert S(create_update_user) == update_user.json()
    assert update_user.json()["name"] == "sant"
    assert update_user.json()["job"] == "aqa"


def test_update_user_by_patch(reqres):
    update_user = reqres.put("api/users/2", {"name": "asantalov", "job": "manual_tester"})

    assert update_user.status_code == 200
    assert S(create_update_user) == update_user.json()
    assert update_user.json()["name"] == "asantalov"
    assert update_user.json()["job"] == "manual_tester"


def test_delete_user(reqres):
    delete_user = reqres.delete("api/users/2")

    assert delete_user.status_code == 204


def test_successful_register(reqres):
    user_register = reqres.post("api/register", {"email": "eve.holt@reqres.in", "password": "pistol"})

    assert user_register.status_code == 200
    assert S(register_user) == user_register.json()
    assert user_register.json()['id']
    assert user_register.json()['token']


def test_unsuccessful_register(reqres):
    user_register = reqres.post("api/register", {"email": "sydney@fife"})

    assert user_register.status_code == 400
    assert S(unregister_user) == user_register.json()
    assert user_register.json()['error'] == 'Missing password'
