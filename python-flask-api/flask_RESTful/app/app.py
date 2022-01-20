from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'CHT89012LciotzHga'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # auth

items = []


class Student(Resource):
    def get(self, name):
        return {'student': name}


class Item(Resource):
    @jwt_required()
    def get(self, name):
        # next will return just the first item in this list that I know that just have one item
        item = next(filter(lambda item: item['name'] == name, items), None)
        return {'item': item}, 200 if item is not None else 404

    def post(self, name):
        if next(filter(lambda item: item['name'] == name, items), None):
            return {'message': "item with this name '{}' already exists".format(name)}, 400

        data = request.get_json()
        items.append({'name': name, 'price': data['price']})
        return {'items': items}, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}, 200


# http://127.0.0.1:5000/student/Leo
api.add_resource(Student, '/student/<string:name>')
api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
