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
    # dataQ = request.form.get('q')
    # return Response(dataQ)
    # value = request.values.get('update_id');
    # message = request.values.get('message')
    content = request.get_json()
    # print (content['update_id'])
    update_id = content['update_id']
    # print str(update_id)
    url = 'https://api.telegram.org/bot' + bot + '/sendMessage'
    data = {'chat_id': '-48348130', 'text': str(update_id), 'disable_notification': 1}
    requests.post(url, data)
    return Response(str(update_id))
    # return Response(['update_id:' + update_id, ' message:' + message])
    # for key, value in value.items():
    #     return key, value


# @app.route(token + 'joke', methods=['POST'])
# def joke():
#     # dataQ = request.form.get('q')
#     # return Response(dataQ)
#     return 'Joke'
#
#
# @app.route(token + 'news', methods=['POST'])
# def news():
#     # dataQ = request.form.get('q')
#     # return Response(dataQ)
#     return 'News'
#
#
# @app.route(token + 'hello', methods=['POST'])
# def hello():
#     # dataQ = request.form.get('q')
#     # return Response(dataQ)
#     return 'Hello'
#
#
# @app.route(token + 'greet', methods=['POST'])
# def greet():
#     # dataQ = request.form.get('q')
#     # return Response(dataQ)
#     return 'Greet El Presidente!!!'
#
#
# @app.route(token + 'birthdays', methods=['POST'])
# def birthdays():
#     # dataQ = request.form.get('q')
#     # return Response(dataQ)
#     return 'List of birthdays'


if __name__ == '__main__':
    app.run(debug=True)
