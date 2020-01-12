#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Bad request', 400
    # 会返回系统状态码 400








if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
