# example/__init__.py
from flask import Flask

def create_app(config):
    from .view import api_user
    from .view import api_article
    
    app = Flask(__name__)
    app.register_blueprint(api_user)
    app.register_blueprint(api_article)
    return app