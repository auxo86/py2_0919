# encoding=utf8
from flask import Flask,  render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('./hello.html',
                           message='pass data to flask using python')


if __name__ == '__main__':
    app.run(port=5000, debug=True)