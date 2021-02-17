# compose_flask/app.py
from flask import Flask
from redis import Redis
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route('/')
def hello():
    mydb = mysql.connector.connect(
        host="db",
        user="compta",
        password="password",
        database='classicmodels'
    )
    print(mydb)

    engine = create_engine('mysql://compta:password@db:3306/classicmodels')


    return ' - - - great has viewed {} time(s) - - -'.format('coucou')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
