import sys, os
import json
from flask import Flask
from flask import render_template

app = Flask(__name__)

print('coucou')

#route for home page
@app.route("/")
def index():
    return "BG"

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)





if __name__ == "__main__":
    app.run(debug=True, port=5000)


