from .conftest import *

def test_server_one():
    app = create_app()
    assert app is not None

def test_server_two(flask_app):
    app = flask_app
    assert app is not None