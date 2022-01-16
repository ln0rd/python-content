from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Student(Resource):
    def get(self, name):
        return {'student': name}


class Item(Resource):
    def get(self, name):
        for item in items:
            if item.name == name:
                return item
        return {'response': 'any item with this name'}

    def post(self, name, price):
        items.append({'name': name, 'price': price})
        return items


# http://127.0.0.1:5000/student/Leo
api.add_resource(Student, '/student/<string:name>')
api.add_resource(Item, '/items/<string:name>')

app.run(port=5000)
