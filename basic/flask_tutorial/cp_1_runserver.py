# copyright : homekeeper89@gmail.com
# 플라스크 기본 구동 방법을 배우는 곳
# example/flask_tutorial/cp_1_runserver.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HELLO WORLD'

if __name__=='__main__':
    app.run()
