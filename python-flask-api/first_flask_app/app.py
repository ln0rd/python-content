from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [
    {'name': 'Tavern Store', "items": [
        {
            'name': 'sword',
            'price': 15.99
        },
        {
            'name': 'silver shield',
            'price': 40.33
        }
    ]}
]


@app.route('/')
def home():
    return 'Hello World'


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': request_data['itens']
    }

    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/')
def get_stores():
    return jsonify({"stores": stores})


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)

    return jsonify({"We have a problem": "Any store with this name has been found"})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            print(new_item)
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message': 'Not identified store'})


app.run(port=5000)
