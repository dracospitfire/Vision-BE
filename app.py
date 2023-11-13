import sys
from gunicorn.app.wsgiapp import run
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

if __name__ == '__main__':
    sys.argv = "gunicorn --bind 0.0.0.0:5151 app:app".split()
    sys.exit(run())
