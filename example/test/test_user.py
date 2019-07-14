from .conftest import *

class TestUser:

    def test_user_register(self, flask_client):
        API = '/user/'
        data = {
            'EMAIL' : 'JAKE@gmail.com',
            'JOB' :'BackEnd',
            'FAVORITE' : 'Python',
            'PWD' :'BestPython'
        }
        res = flask_client.post(API, data=json.dumps(data))
        assert res.status_code == 200

    def test_user_login(self, flask_client):
        data = {
            'EMAIL' : 'JAKE@gmail.com',
            'PWD' :'BestPython'
        }
        API = '/user/{}'.format(data['EMAIL'])
        res = flask_client.get(API,data=json.dumps(data), headers = JSON_HEADER)
        assert res.status_code == 200