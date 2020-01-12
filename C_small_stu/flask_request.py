#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your brower is {}</p>'.format(user_agent)
    # 获得的是请求头浏览器的信息
    # Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)
