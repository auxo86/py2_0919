# encoding=utf8
from flask import Flask


app = Flask(__name__)


@app.route('/<int:count>/hi/<name>')
def hello_name(count, name):
    str='Hello'
    for i in range(0, count):
        str += '%s'% name

    return str

# http://127.0.0.1:5678/mypath/3.14159/can/be/any/direcxtory
# can/be/any/direcxtory就是goal
@app.route('/mypath/<float:weight>/<path:goal>')
def hello_name2(goal, weight):
    str = 'my data = %f, %s' % (weight, goal)
    return str

if __name__ == '__main__':
    app.run(port=5678, host='0.0.0.0', debug=True)