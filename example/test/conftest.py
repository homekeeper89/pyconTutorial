# example/test/conftest.py

from . import *

@pytest.fixture(scope='session')
def flask_app():
    """create_app을 만드는 픽스쳐"""
    app = create_app('dev')
    app_context = app.app_context()
    app_context.push()

    yield app
    app_context.pop()

@pytest.fixture(scope='session')
def flask_client(flask_app):
    """테스트를 위한 클라이언트"""
    return flask_app.test_client()