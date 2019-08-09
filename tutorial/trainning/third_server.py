from flask import Blueprint, Flask

my_page = Blueprint('my_page', __name__, url_prefix='/page')
my_user = Blueprint('my_user', __name__)

@my_page.route('/')
def blue_mypage():
    return 'I am blue mypage'

@my_user.route('/')
def blue_myuser():
    return 'I am blue myuser'


app = Flask(__name__)
app.register_blueprint(my_page)
app.register_blueprint(my_user, url_prefix = '/user')

if __name__ == '__main__':
    app.run(debug=True)


