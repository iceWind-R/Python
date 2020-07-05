import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
    f = open('index.html', 'rb')
    data = f.read()
    f.close()
    return data

@app.route('/hi')
def hi():
    return 'hi'

app.run()