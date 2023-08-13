import os

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/blogs')
def blogs():
    return jsonify([
        {'id': 1, 'title': 'My first blog', 'content': 'Hello, this is my first blog!'},
        {'id': 2, 'title': 'Second post', 'content': 'Here goes the second blog.'}
    ])


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("build/" + path):
        return send_from_directory('build', path)
    else:
        return send_from_directory('build', 'index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

    # npm run build
