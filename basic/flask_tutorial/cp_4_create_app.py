from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)

    from cp_3_view import my_page
    from cp_3_view import my_store
    app.register_blueprint(my_page)
    app.register_blueprint(my_store, url_prefix='/products')

    return app


if __name__ =='__main__':
    app = create_app('dev')
    app.run()