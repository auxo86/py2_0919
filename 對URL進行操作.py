# encoding=utf8
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/tiger')
def hello_tiger():
    return '[T] I am a tiger'


@app.route('/lion')
def hello_lion():
    return '[L] I am a lion'


@app.route('/new/<animal>')
def hello_animal(animal):
    return '[A] Hello %s' % animal


@app.route('/animal/<kind>')
def hello_any(kind):
    if kind == 'tiger':
        return redirect(url_for('hello_tiger'))
    elif kind == 'lion':
        return redirect(url_for('hello_lion'))
    else:
        # redirect()的參數寫在後面
        return redirect(url_for('hello_animal', animal=kind))


if __name__ == '__main__':
    app.run(port=5678, host='0.0.0.0', debug=True)