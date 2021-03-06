# compose_flask/app.py
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis-container', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return ' - - - great has viewed {} time(s) - - -'.format(redis.get('hits'))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
