from flask import Flask, request, jsonify

app=Flask(__name__)

# Initial Data in my Todo List.
items = [
      {
            "id": 1,
            "name": "Item ",
            "description": "This is Item "
      },
      {
            "id": 2,
            "name": "Item 2",
            "description": "This is Item 2"
      },
      {
            "id": 3,
            "name": "Item 3",
            "description": "This is Item 3"
      }
]

@app.route('/')
def home():
      return "Welcome to the sample Todo List app"

@app.route('/items', methods=['GET'])
def get_items():
      return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
      item = next((item for item in items if item["id"] == item_id), None)
      if item is None:
            return jsonify({"error": "Item not found"}), 404
      return jsonify(item)

@app.route('/items', methods=['POST'])
def create_item():
      if not request.json:
            return jsonify({"error": "No data provided"}), 400
      if not all(key in request.json for key in ['name', 'description']):
            return jsonify({"error": "Missing required fields"}), 400
            
      new_item = {
            "id": items[-1]["id"] + 1 if items else 1,
            "name": request.json['name'],
            "description": request.json['description']
      }
      items.append(new_item)
      return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
      item = next((item for item in items if item["id"] == item_id), None)
      if item is None:
            return jsonify({"error": "Item not found"}), 404
      if not request.json:
            return jsonify({"error": "No data provided"}), 400
            
      item['name'] = request.json.get('name', item['name'])
      item['description'] = request.json.get('description', item['description'])
      return jsonify(item)
      
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
      global items
      item = next((item for item in items if item["id"] == item_id), None)
      if item is None:
            return jsonify({"error": "Item not found"}), 404
      items = [item for item in items if item["id"] != item_id]
      return '', 204

if __name__ == '__main__':
      app.run(debug=True)