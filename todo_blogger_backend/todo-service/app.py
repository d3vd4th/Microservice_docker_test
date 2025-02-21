from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []
next_id = 1

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    global next_id
    data = request.get_json()
    todo = {
        'id': next_id,
        'title': data.get('title'),
        'done': False
    }
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['title'] = data.get('title', todo['title'])
            todo['done'] = data.get('done', todo['done'])
            return jsonify(todo), 200
    return jsonify({"error": "Todo not found"}), 404

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({"msg": "Todo deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
