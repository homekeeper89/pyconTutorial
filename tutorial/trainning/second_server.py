from flask import Flask

app = Flask('hellworld') # __name__


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'HELLO WORLD'

@app.route('/<username>')
def hello_user(username):
    return 'I am ' + username

@app.route('/holly')
def hello_hollys():
    return 'I am hollys'

@app.route('/page/<int:number>')
def page(number):
    return 'I am ' + str(number)


if __name__ =='__main__':
    app.run(debug=True)

