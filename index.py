#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask

app = Flask(__name__)


@app.route("/index")
def index():
    return "Index Page!"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
