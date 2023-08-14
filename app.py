"""
Main backend for the app.
"""
import os

from flask import Flask, jsonify, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__, static_folder="blog-frontend/build")

# Replace postgres:// with postgresql:// for SQLAlchemy compatibility
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///local_db.db')
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
CORS(app, resources={r"/api/*": {"origins": "*"}})
db = SQLAlchemy(app)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)


@app.route('/api/blogs', methods=['GET', 'POST'])
def handle_blogs():
    if request.method == 'GET':
        blogs = Blog.query.all()
        return jsonify([{"id": blog.id, "title": blog.title, "content": blog.content} for blog in blogs])

    elif request.method == 'POST':
        blog_data = request.json
        new_blog = Blog(title=blog_data['title'], content=blog_data['content'])
        db.session.add(new_blog)
        db.session.commit()
        return jsonify({"id": new_blog.id, "title": new_blog.title, "content": new_blog.content}), 201


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
