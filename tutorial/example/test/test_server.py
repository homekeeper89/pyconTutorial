# example/test/test_server.py

from .conftest import *

class TestServer:

    def test_server_one(self):
        app = create_app()
        assert app is not None

    def test_server_two(self, flask_app):
        app = flask_app
        assert app is not None
        