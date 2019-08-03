#app/test/__init__.py
import pytest
from app import create_app

import json
JSON_HEADER = {'content-type':"application/json"}