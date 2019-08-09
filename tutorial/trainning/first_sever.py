from flask import Flask

app = Flask('hellworld') # __name__

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'HELLO WORLD'

if __name__ =='__main__':
    app.run()

