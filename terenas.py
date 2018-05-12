from flask import Flask, request
from werkzeug.wrappers import Response
from settings import token, bot
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
    update_id = content['update_id']
    command = content['message']['text']
    url = 'https://api.telegram.org/bot' + bot + '/sendMessage'
    if command == '/hello':
        text = 'Hello everyone, I`m working now'
    elif command == '/birthdays':
        text = 'Тут будет список ДР'
    elif command == '/greet':
        text = 'Всякие приветствия Эль Президенте и не только'
    elif command == '/news':
        text = 'Новости, ну вы поняли'
    elif command == '/joke':
        text = 'Шутейки'
    else:
        return Response(False)
    data = {'chat_id': '-48348130', 'text': text, 'disable_notification': 1}
    requests.post(url, data)
    return Response(True)


if __name__ == '__main__':
    app.run(debug=True)
