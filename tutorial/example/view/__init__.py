# example/view/__init__.py

import json
from flask import Blueprint, Flask, request, jsonify, session
from mock_database import *

USER_FILE = 'common_user.json'
ARTICLE_FILE = 'common_article.json'

api_user = Blueprint('user', __name__, url_prefix='/user')
api_article = Blueprint('article', __name__, url_prefix='/article')

def session_checker(session):
    if session['SERVER_MSG'] == 'LOGIN_SUCCESS':
        return True
    return False

from .user import *
from .article import *