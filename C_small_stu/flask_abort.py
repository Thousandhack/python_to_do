#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route('/user/<id>/')
def index(id):
    print(id)
    user_dict = {
        1: "hsz",
        2: "zero",
        3: "one"
    }
    user = user_dict[int(id)]
    print(user)
    if not user:
        abort(404)
    return '<h1>Hello,{}</h1>'.format(user)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
