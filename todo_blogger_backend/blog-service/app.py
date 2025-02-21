from flask import Flask, request, jsonify

app = Flask(__name__)

posts = []
next_id = 1

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts), 200

@app.route('/posts', methods=['POST'])
def add_post():
    global next_id
    data = request.get_json()
    post = {
        'id': next_id,
        'title': data.get('title'),
        'content': data.get('content')
    }
    posts.append(post)
    next_id += 1
    return jsonify(post), 201

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    for post in posts:
        if post['id'] == post_id:
            post['title'] = data.get('title', post['title'])
            post['content'] = data.get('content', post['content'])
            return jsonify(post), 200
    return jsonify({"error": "Post not found"}), 404

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return jsonify({"msg": "Post deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
