
from flask import Blueprint, render_template, abort, Flask

my_page = Blueprint('my_page', __name__, url_prefix="/users")
my_store = Blueprint('my_store', __name__)

@my_page.route('/<int:path>')
def getUsers(path):
    return 'users route ' + str(path)

@my_store.route('/<products>')
def getProducts(products):
    return 'MyStore route ' + products

app = Flask(__name__)
app.register_blueprint(my_page)
app.register_blueprint(my_store, url_prefix='/products')


if __name__ =='__main__':
    app.run(debug=True)