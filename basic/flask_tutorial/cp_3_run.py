from flask import Flask
from cp_3_view import *

app = Flask(__name__)
app.register_blueprint(my_page)
app.register_blueprint(my_store, url_prefix='/products')


if __name__ =='__main__':
    app.run(debug=True)