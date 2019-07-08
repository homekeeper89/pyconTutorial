# example/view/__init__.py

import json
from flask import Blueprint, Flask, request

api_user = Blueprint('user', __name__, url_prefix='/user')

from .user import *