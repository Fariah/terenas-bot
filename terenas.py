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
    return Response(content)
    # command = content['message']['text']
    # url = 'https://api.telegram.org/bot' + bot + '/sendMessage'
    # if command == '/hello':
    #     text = 'Hello, I`m working now.'
    # elif command == '/start':
    #     return Response(1)
    # elif command == '/birthdays':
    #     text = 'The list of Birthdays.'
    # elif command == '/greet':
    #     text = 'Greet El Presidente!!!'
    # elif command == '/news':
    #     text = 'News news news.'
    # elif command == '/joke':
    #     text = 'Jokes and funny stories'
    # else:
    #     return Response(1)
    # data = {'chat_id': chat_id, 'text': text, 'disable_notification': 1}
    # requests.post(url, data)
    # return Response(1)


if __name__ == '__main__':
    app.run(debug=True)
