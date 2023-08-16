"""
Main backend for the app.
"""
import os

from flask import Flask, jsonify, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__, static_folder="blog-frontend/build")

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///local_db.db")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
CORS(app, resources={r"/api/*": {"origins": "*"}})
db = SQLAlchemy(app)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    position = db.Column(db.Integer, nullable=True)


@app.route("/api/blogs", methods=["GET", "POST"])
def handle_blogs():
    if request.method == "GET":
        blogs = Blog.query.all()
        return jsonify(
            [
                {
                    "id": blog.id,
                    "title": blog.title,
                    "content": blog.content,
                    "position": blog.position if blog.position is not None else blog.id,
                }
                for blog in sorted(
                    blogs, key=lambda x: x.position if x.position is not None else x.id
                )
            ]
        )

    if request.method == "POST":
        blog_data = request.json
        if not blog_data or "title" not in blog_data or "content" not in blog_data:
            return jsonify({"error": "Invalid data provided"}), 400
        try:
            new_blog = Blog(title=blog_data["title"], content=blog_data["content"])
            highest_position = (
                db.session.query(db.func.max(Blog.position)).scalar() or 0
            )
            new_blog.position = highest_position + 1
            db.session.add(new_blog)
            db.session.commit()
            return (
                jsonify(
                    {
                        "id": new_blog.id,
                        "title": new_blog.title,
                        "content": new_blog.content,
                        "position": new_blog.position,
                    }
                ),
                201,
            )
        except:
            db.session.rollback()
            return jsonify({"error": "Error saving the blog"}), 500

    return jsonify({"error": "Method not allowed"}), 405


@app.route("/api/blogs/<int:blog_id>", methods=["PUT"])
def handle_update_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if not blog:
        return jsonify({"error": "Blog not found"}), 404

    blog_data = request.json
    if not blog_data or "title" not in blog_data or "content" not in blog_data:
        return jsonify({"error": "Invalid data provided"}), 400
    try:
        blog.title = blog_data["title"]
        blog.content = blog_data["content"]
        db.session.commit()
        return (
            jsonify(
                {
                    "id": blog.id,
                    "title": blog.title,
                    "content": blog.content,
                    "position": blog.position,
                }
            ),
            200,
        )
    except:
        db.session.rollback()
        return jsonify({"error": "Error updating the blog"}), 500


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")


@app.errorhandler(404)
def not_found(error):  # pylint: disable=unused-argument
    return jsonify({"error": {"Not found"}}), 404


@app.errorhandler(500)
def internal_error(error):  # pylint: disable=unused-argument
    return jsonify({"error": {"Internal server error"}}), 500


if __name__ == "__main__":
    try:
        with app.app_context():
            db.create_all()
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    except Exception as e:
        print(f"Failed to run the app: {str(e)}")
