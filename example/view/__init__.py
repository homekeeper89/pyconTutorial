# example/view/__init__.py

import json
from flask import Blueprint, Flask, request
from mock_database import *

USER_FILE = 'common_user.json'
ARTICLE_FILE = 'common_article.json'

api_user = Blueprint('user', __name__, url_prefix='/user')
api_article = Blueprint('article', __name__, url_prefix='/article')

from .user import *
from .article import *