# view/__init__.py
from flask import Blueprint, request

user_api = Blueprint('user_api', __name__, url_prefix='/user')

from mock_database import *
USER_FILE = 'common_user.json'
ARTICLE_FILE = 'common_article.json'
from .user import *