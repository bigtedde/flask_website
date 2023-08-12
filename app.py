from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/blogs')
def blogs():
    return jsonify([
        {'id': 1, 'title': 'My first blog', 'content': 'Hello, this is my first blog!'},
        {'id': 2, 'title': 'Second post', 'content': 'Here goes the second blog.'}
    ])


if __name__ == "__main__":
    app.run(debug=True)
