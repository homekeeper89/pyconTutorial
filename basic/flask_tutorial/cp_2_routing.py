# copyright : homekeeper89@gmail.com
# 플라스크 기본 구동 방법을 배우는 곳
#
#

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HELLO WORLD'

@app.route('/a')
def route_a():
    return 'I am a'

@app.route('/b')
def route_b():
    return 'I am b'

@app.route('/user/<username>')
def route_username(username):
    return 'I am ' + username

@app.route('/page/<int:page>')
def route_pate(page):
    return 'I want this page ' + str(page)

if __name__=='__main__':
    app.run()
