from flask import Flask, request
from werkzeug.wrappers import Response
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World! It`s home page'


@app.route('/test', methods=['POST'])
def test():
    data = request.form.get('q')
    return Response(data)


if __name__ == '__main__':
    app.run(debug=True)
