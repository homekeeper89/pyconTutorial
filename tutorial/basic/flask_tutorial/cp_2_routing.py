# copyright : homekeeper89@gmail.com
# routing : client의 요청을 내가 원하는 함수(control 또는  view)로 연결해주는 것

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
def route_page(page):
    return 'I want this page ' + str(page)

@app.route('/name/<string:name>')
def route_name(name):
    return 'I am route ' + name

@app.route('/path/<path:whatever_any_path>')
def route_any_path(whatever_any_path):
    return 'I am path ' + whatever_any_path

if __name__=='__main__':
    app.run(debug=True)
