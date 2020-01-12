#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Hello world!</h1>'


@app.route("/user/<name>/")
def user(name):
    return '<h1>Hello {}!</h1>'.format(name)


if __name__ == '__main__':
    # debug=True 表示调试模式
    app.run(host='127.0.0.1', port=5000, debug=True)
