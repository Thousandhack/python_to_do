#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask
from flask import request

app = Flask(__name__)


# methods=['get', 'post', 'put', 'delete'] 表示允许访问的方法
@app.route('/method', methods=['get', 'post', 'put', 'delete'])
def index():
    # 打印请求方法
    print(request.method)
    """
    get 的时候打印：
    GET
    
    post的时候：
    POST
    
    put的时候：
    PUT
    
    delete的时候：
    DELETE
    """
    return 'method ok'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
