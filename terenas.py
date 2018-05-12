import os
import random

from flask import Flask, request
from werkzeug.wrappers import Response
from settings import token, bot, chat_id
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Hello World! It`s home page of Flask'


@app.route('/check/<code>', methods=['GET'])
def check(code):
    if code == token.strip('/'):
        return Response('Token is correct')
    return Response('Token is invalid')


@app.route(token, methods=['POST'])
def bot_handler():
    content = request.get_json()
    command = content['message']['text']
    url = 'https://api.telegram.org/bot' + bot + '/sendMessage'
    if command == '/hello':
        text = 'Hello, I`m working now.'
    elif command == '/start':
        return Response(str(1))
    elif command == '/birthdays':
        text = 'The list of Birthdays.'
    elif command == '/greet':
        text = 'Greet El Presidente!!!'
    elif command == '/news':
        text = 'News news news.'
    elif command == '/joke':
        with open(os.path.dirname(os.path.abspath(__file__)) + '/jokes.txt', 'r') as myfile:
            data = myfile.read().split('#')
        num_string = random.randint(0, 10)
        text = data[num_string]
    else:
        return Response(str(2))
    data = {'chat_id': chat_id, 'text': text, 'disable_notification': 1}

    requests.post(url, data)
    return Response(str(3))


if __name__ == '__main__':
    app.run(debug=True)
