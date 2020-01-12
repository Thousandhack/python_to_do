#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route("/post", methods=['post'])
def get_post():
    """2.获取请求体请求数据"""
    print(request.data)
    data = json.loads(request.data)
    print(data)  # 结果： {'username': 'xiaoming', 'pwd': '123456'}  在flask版本较低中使用
    """
    访问地址：http://0.0.0.0:9000/post
    接收效果：b'{\n\t"username":"xiaoming",\n\t"pwd":"123456"\n}'
    """
    """ 直接获取json数据"""
    print(request.json)  # 0.10版本以下没有
    """
    参数：JSON
    {
        'username': 'xiaoming', 
        'pwd': '123456'
    }
    """
    return "post ok"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)