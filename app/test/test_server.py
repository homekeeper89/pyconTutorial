from . import *

def test_server_run():
    app = create_app()
    assert app is not None

def test_server_fixture(flask_app):
    app = flask_app
    assert app is not None