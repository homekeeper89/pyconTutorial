# example/test/conftest.py

from . import *

@pytest.fixture
def flask_app():
    """create_app을 만드는 픽스쳐"""
    app = create_app('dev')
    app.config['SECRET_KEY'] = 'sekrit!'
    app_context = app.app_context()
    app_context.push()

    yield app
    app_context.pop()

@pytest.fixture
def flask_client(flask_app):
    """테스트를 위한 클라이언트"""
    return flask_app.test_client()

@pytest.fixture(
    params=[
        {"EMAIL": "jake@gmail.com", 'PWD':'BestPython'},
    ]
)
def flask_client_login(flask_client,request):
    API = '/user/{}'.format(request.param['EMAIL'])
    DATA = request.param
    res = flask_client.get(API,data=json.dumps(DATA), headers = JSON_HEADER)
    if res.status_code == 200:
        with flask_client.session_transaction() as server_session:
            server_session['EMAIL'] = request.param['EMAIL']
            server_session['SERVER_MSG'] = json.loads(res.get_data())['SERVER_MSG']
        yield flask_client
    
    # with flask_client:
    #     with flask_client.session_transaction() as ss:
    #         ss['EMAIL'] = request.param['EMAIL']
    #         ss['SERVER_MESSAGE'] = 'LOGIN_SUCCESS'
    #     yield flask_client
