from flask import Flask, request, Response, jsonify
import requests
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key' 
jwt = JWTManager(app)

SERVICE_MAP = {
    'auth': 'http://auth-service:5000',
    'todos': 'http://todo-service:5000',
    'posts': 'http://blog-service:5000'
}

def proxy_request(target_url):
    resp = requests.request(
        method=request.method,
        url=target_url,
        headers={key: value for key, value in request.headers if key.lower() != 'host'},
        params=request.args,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False
    )
    # Exclude certain headers from the proxied response
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]
    return Response(resp.content, resp.status_code, headers)

# Forward auth endpoints without JWT validation
@app.route('/auth/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def auth_proxy(path):
    target_url = f"{SERVICE_MAP['auth']}/{path}"
    return proxy_request(target_url)

# Protect these endpoints at the gateway level
@app.route('/todos', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/todos/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@jwt_required()
def todos_proxy(path):
    user = get_jwt_identity()  # For logging or enrichment purposes
    print(f"Authenticated user for todos: {user}")
    target_url = f"{SERVICE_MAP['todos']}/todos"
    if path:
        target_url += f"/{path}"
    return proxy_request(target_url)

@app.route('/posts', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/posts/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@jwt_required()
def posts_proxy(path):
    user = get_jwt_identity()
    print(f"Authenticated user for posts: {user}")
    target_url = f"{SERVICE_MAP['posts']}/posts"
    if path:
        target_url += f"/{path}"
    return proxy_request(target_url)

# Optional: a simple endpoint to verify token validity.
@app.route('/verify', methods=['GET'])
@jwt_required()
def verify_token():
    user = get_jwt_identity()
    return jsonify({"msg": "Token is valid", "user": user}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
