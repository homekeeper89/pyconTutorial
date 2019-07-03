
from flask import Blueprint, render_template, abort, Flask

my_page = Blueprint('my_page', __name__, url_prefix="/users")

@my_page.route('/', defaults={'path': 'default'})
@my_page.route('/<path:path>')
def show(page):
    """ /로 들어올 경우 page의 기본값은 index가 된다
    /something 으로 들어올 경우 page 자리에 someting이 간다
    """
    return 'i am ' + page

app = Flask(__name__)
app.register_blueprint(my_page)


if __name__ =='__main__':
    app.run(debug=True)