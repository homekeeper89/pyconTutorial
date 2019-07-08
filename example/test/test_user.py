from .conftest import *

class TestUser:

    def test_user_register(self, flask_client):
        API = '/user/'
        data = {
            'NAME' : 'JAKE',
            'JOB' :'BackEnd',
            'FAVORITE' : 'Python'
        }
        res = flask_client.post(API, data=json.dumps(data))
        assert res.status_code == 200