# encoding=utf8
from flask import Flask
from flask_restful import Resource, Api

app=Flask(__name__)
api = Api(app)

class Rest1(Resource):
    def get(self):
        return {'key1':'hello', 'key2':'world', 'key3':3.14, 'key4':['Mark', 'Python', 12345, '中文輸入']}

class Rest2(Resource):
    def get(self):
        return ['Mark', 'Python', 12345, '中文輸入', {'key1':'hello', 'key2':'world', 'key3':3.14, 'key4':['Mark', 'Python', 12345, '中文輸入']}]

api.add_resource(Rest1, '/rest1')
api.add_resource(Rest2, '/rest2')

if __name__ == '__main__':
    app.run(port=5678, host='0.0.0.0', debug=True)