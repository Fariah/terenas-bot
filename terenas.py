from flask import Flask, request
from werkzeug.wrappers import Response
from settings import token

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Hello World! It`s home page of Flask'


@app.route('/check/<code>', methods=['GET'])
def check(code):
    if code == token.strip('/'):
        return Response('Token is correct')
    return Response('Token is invalid')


@app.route(token + 'joke', methods=['POST'])
def test():
    # dataQ = request.form.get('q')
    # return Response(dataQ)
    return 'Joke'


@app.route(token + 'news', methods=['POST'])
def test():
    # dataQ = request.form.get('q')
    # return Response(dataQ)
    return 'News'


@app.route(token + 'hello', methods=['POST'])
def test():
    # dataQ = request.form.get('q')
    # return Response(dataQ)
    return 'Hello'


@app.route(token + 'greet', methods=['POST'])
def test():
    # dataQ = request.form.get('q')
    # return Response(dataQ)
    return 'Greet El Presidente!!!'


@app.route(token + 'birthdays', methods=['POST'])
def test():
    # dataQ = request.form.get('q')
    # return Response(dataQ)
    return 'List of birthdays'


if __name__ == '__main__':
    app.run(debug=True)
