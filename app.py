from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
    return "Welcome to my blog!"


@app.route('/api/blogs')
def blogs():
    return jsonify([
        {'id': 1, 'title': 'My first blog', 'content': 'Hello, this is my first blog!'},
        {'id': 2, 'title': 'Second post', 'content': 'Here goes the second blog.'}
    ])


if __name__ == "__main__":
    app.run(debug=True)
