#app/test/test_user.py
from . import *

def test_client_login(flask_client):
    res = flask_client.get('/login')
    assert res.status_code == 200

def test_user_login(flask_client):
    data = {
        "PWD": "BestPython"
    }
    data = json.dumps(data)
    res = flask_client.post('/user/jake@gmail.com', data=data, headers=JSON_HEADER)
    assert res.status_code == 200
    assert res.json['SERVER_MSG'] == 'LOGIN_SUCCESS'

def test_user_register(flask_client):
    data = {
        "EMAIL": "jake@gmail.com",
        "JOB": "BackEnd",
        "FAVORITE": "Python",
        "PWD": "BestPython"
    }
    data = json.dumps(data)
    res = flask_client.post('/user/register', data=data, headers = JSON_HEADER)
    assert res.status_code == 200
    assert json.loads(res.get_data())['RES'] == 'SUCCESS'