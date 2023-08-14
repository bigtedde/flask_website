"""
Main backend for the app.
"""
import os

from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS

app = Flask(__name__, static_folder="blog-frontend/build")
CORS(app, resources={r"/api/*": {"origins": "*"}})


blogs_list = [
    {"id": 1, "title": "My first blog", "content": "Hello, this is my first blog!"},
    {"id": 2, "title": "Second post", "content": "Here goes the second blog."},
]


@app.route('/api/blogs', methods=['GET', 'POST'])
def handle_blogs():
    if request.method == 'GET':
        return jsonify(blogs_list)
    elif request.method == 'POST':
        blog = request.json
        blog['id'] = len(blogs_list) + 1
        blogs_list.append(blog)
        return jsonify(blog), 201



@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    # npm run build
