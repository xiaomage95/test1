from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return 'index111'


if __name__ == '__main__':
    app.run(debug=True)
