from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Python flask 0919"
@app.route('/welcome')
def welcome():
    return "welcome back to learn python, Today we learn flask"

if __name__ == '__main__':
    app.run(port=5678, debug=True)
