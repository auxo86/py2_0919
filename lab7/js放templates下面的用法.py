from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./hello.html', data=[10,20,30,40,50])

if __name__ == '__main__':
    app.run(port=5556, host='0.0.0.0', debug=True)