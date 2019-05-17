# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/
import os
import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    ipaddr = socket.gethostbyname(socket.gethostname())
    return 'Im  Chitti v2.0 ! \n IP Address '+ipaddr

if __name__ == '__main__':
#    app.run()
    app.run(host='0.0.0.0', port=os.environ.get('listenport', 8080))

