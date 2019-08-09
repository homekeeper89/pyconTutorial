# app/__init__.py
# 해당 폴더경로에서 공통적으로 쓰이는 부분을 전부 여기에 넣을꺼에요.
# 공통적으로쓰인다는 것은 모듈 또는 함수 등이 됩니다.

from flask import Flask

def create_app():
    app = Flask(__name__)
    return app 