from .conftest import *

def test_client(flask_client):
    res = flask_client.get('/user/login')
    assert res.status_code == 200

def test_client_register(flask_client):
    data = {
        "EMAIL": "jake@gmail.com",
        "JOB": "BackEnd",
        "FAVORITE": "Python",
        "PWD": "BestPython"
    }
    res = flask_client.post('/user/register', data = json.dumps(data), headers=JSON_HEADER)
    assert res.status_code == 200
    assert res.json['res'] == 'SUCCESS'