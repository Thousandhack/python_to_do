#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/headers', methods=['get', 'post'])
def headers():
    # 获取请求头的数据
    print(request.headers)
    """
    访问链接：
    http://127.0.0.1:9000/headers
    
    打印内容：
    Content-Type: application/x-www-form-urlencoded
    User-Agent: PostmanRuntime/7.21.0
    Accept: */*
    Cache-Control: no-cache
    Postman-Token: 869ac15a-2648-4042-bb7a-9463666e9208
    Host: 127.0.0.1:9000
    Accept-Encoding: gzip, deflate
    Content-Length: 43
    Connection: keep-alive
    """
    #
    print(request.headers.get('Content-Type'))
    """
    打印内容：
    application/x-www-form-urlencoded
    """

    # 例2：获取自定义的请求头信息
    print(request.headers.get('Cpwd'))
    """
    参数：在Headers上加键值对：  Cpwd     ewqoeuqieq1231313
    打印内容：
    ewqoeuqieq1231313
    """
    return 'header ok'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
