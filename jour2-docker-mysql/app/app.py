# compose_flask/app.py
from flask import Flask
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine

app = Flask(__name__)


@app.route('/')
def hello():
    engine = create_engine('mysql+pymysql://compta:password@db:3306/classicmodels')

    return ' - - - MySQL Database `classicmodels` connection ok - - -'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
