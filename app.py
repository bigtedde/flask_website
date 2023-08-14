"""
Main backend for the app.
"""
import os

from flask import Flask, jsonify, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__, static_folder="blog-frontend/build")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(500))


@app.route('/api/blogs', methods=['GET', 'POST'])
def handle_blogs():
    if request.method == 'GET':
        blogs = Blog.query.all()
        return jsonify([{'id': blog.id, 'title': blog.title, 'content': blog.content} for blog in blogs])
    elif request.method == 'POST':
        new_blog = Blog(title=request.json['title'], content=request.json['content'])
        db.session.add(new_blog)
        db.session.commit()
        return jsonify({'id': new_blog.id, 'title': new_blog.title, 'content': new_blog.content}), 201


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    db.create_all()  # Creates blogs.db if not exists
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
