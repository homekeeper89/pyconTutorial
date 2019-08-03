# app / __init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)
    from .view import user_api
    app.register_blueprint(user_api)
    return app