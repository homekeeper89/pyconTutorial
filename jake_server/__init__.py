from flask import Flask, request

def create_app():
    app = Flask(__name__)
    from .view import user_api
    app.register_blueprint(user_api)
    return app