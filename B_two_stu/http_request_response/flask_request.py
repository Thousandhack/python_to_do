#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route("/")
def index():
    # request
    print(request)
    """
    <Request 'http://127.0.0.1:9000/?name=zero&pwd=123' [GET]>
    """
    # 1.获取get参数
    print(request.args)  # 获取查询字符串 也就是url问号后面的
    """
    访问路径：
    http://127.0.0.1:9000/?name=zero&pwd=123
    打印效果：
    ImmutableMultiDict([('name', 'zero'), ('pwd', '123')])
    MultiDict内部实现的是OrderDict字典结构
    from collections import OrderedDict   # 有序字典
    
    
    """
    """
    访问路径：
    http://127.0.0.1:9000/?name=zero&pwd=123&like=sing&like=running
    打印结果：
    zero
    """
    # 获取指定参数的值
    print(request.args.get('name'))  # 打印结果：zero
    """
    访问路径：
    http://127.0.0.1:9000/?name=zero&pwd=123&like=sing&like=running
    打印结果：
    ['sing', 'running']
    """
    # 获取指定参数的多个值，用于接收表单的多选框值  列表类型
    print(request.args.getlist('like'))  # 打印结果：['sing', 'running']

    return 'hello flask'


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
