# example/__init__.py

from flask import Flask

def create_app(config):
    from .view import api_user
    
    app = Flask(__name__)
    app.register_blueprint(api_user)
    return app