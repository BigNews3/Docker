import sys, os
import json
from flask import Flask
from flask import render_template
from flask import jsonify, make_response

app = Flask(__name__)

print('coucou')

#route for home page
@app.route("/")
def index():
    return "BG"

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route("/api/books")
def books():
    with open('db/books.json') as f:
        data = json.load(f)
    return jsonify(data)


@app.route('/api/books/<int:book_id>')
def book_by_id(book_id):
    with open('db/books.json') as f:
        data = json.load(f)

    for book in data:
        if 'isbn' in book and book['isbn'] == str(book_id):
            return jsonify(book)
        return 'null'


@app.route('/api/books/title/<string:title>')
def book_by_title(title):
    with open('db/books.json') as f:
        data = json.load(f)

    for book in data:
        if 'title' in book and book['title'] == title:
            return jsonify(book)
        return 'null'




if __name__ == "__main__":
    app.run(debug=True, port=5000)


