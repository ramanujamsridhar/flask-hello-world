# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/
import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Amex v1.0 !'

if __name__ == '__main__':
#    app.run()
    app.run(host='0.0.0.0', port=os.environ.get('listenport', 8080))

