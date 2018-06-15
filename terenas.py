#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from werkzeug.wrappers import Response
from settings import token, bot, chat_id
import requests
import joke, birthday, greet, news

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
    if command == '/hello' or command == '/hello@terebas_bot':
        text = 'Привет, есть че?'
    elif command == '/start' or command == '/start@terebas_bot':
        return Response(str(1))
    elif command == '/birthdays' or command == '/birthdays@terebas_bot':
        text = birthday.birthdays_list()
    elif command == '/greet' or command == '/greet@terebas_bot':
        text = greet.get_greet()
    elif command == '/news' or command == '/news@terebas_bot':
        text = news.get_news_list()
    elif command == '/joke' or command == '/joke@terebas_bot':
        text = joke.get_joke()
    else:
        text = 'Ты че мне ща сказал? А ну повтори.'
    data = {'chat_id': chat_id, 'text': text, 'disable_notification': 1}

    requests.post(url, data)
    return Response(str(3))


if __name__ == '__main__':
    app.run(debug=True)
