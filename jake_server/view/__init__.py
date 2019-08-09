from flask import Blueprint, request
from mock_database import *

user_api = Blueprint('user', __name__, url_prefix='/user')
USER_FILE = 'common_user.json'
from .user import *