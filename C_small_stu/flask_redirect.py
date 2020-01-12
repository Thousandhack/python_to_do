#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask
from flask import redirect

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('https://www.baidu.com/?tn=96928074_hao_pg')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
