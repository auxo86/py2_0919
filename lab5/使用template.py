# encoding=utf8
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    dict = {'name':'Mark', 'role':'Engineer','position':'Taipei'}
    return render_template('./hello.html',
                           subtitle='Python Lab 5',
                           dataToPass=dict)

if __name__ == '__main__':
    app.run(port=5678, host='0.0.0.0', debug=True)