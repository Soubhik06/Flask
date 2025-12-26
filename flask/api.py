from flask import Flask, jsonify, request
app = Flask(__name__)

##initial data
items = [
    {'id': 1, 'name': 'item1', 'description': 'This is item 1'},
    {'id': 2, 'name': 'item2', 'description': 'This is item 2'},
    {'id': 3, 'name': 'item3', 'description': 'This is item 3'}
]
@app.route('/')
def home():
    return "welcome to the sample to do list app"
## get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

## get item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

##post : create a new task
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({'message': 'Invalid input'}), 400
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'description': request.json.get('description', '')
    }
    items.append(new_item)
    return jsonify(new_item), 201

## put : update an existing item    
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({'message': 'Item not found'}), 404
    if not request.json:
        return jsonify({'message': 'Invalid input'}), 400
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)
## delete : delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'})

if __name__ == "__main__":
    app.run(debug=True)