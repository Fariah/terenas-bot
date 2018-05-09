from flask import Flask, request
from werkzeug.wrappers import Response
from settings import token

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World! It`s home page of Flask'


@app.route(token + 'test', methods=['POST'])
def test():
    dataQ = request.form.get('q')
    return Response(dataQ)


if __name__ == '__main__':
    app.run(debug=True)
