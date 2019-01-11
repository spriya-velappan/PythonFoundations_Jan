"""
title: flask_app
author: sxv3240
date: 1/11/2019 9:12 AM
"""


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"


@app.route("/goodbye")
def goodbye():
    return "GoodBye!"

import os
port = int(os.getenv('PORT',3000))

if __name__ == '__main__':

     app.run(debug=True,host='0.0.0.0',port=port)