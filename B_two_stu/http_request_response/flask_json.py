#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/json")
def json():
    # 也可以响应json格式代码
    data = [
        {"id": 1, "username": "liulaoshi", "age": 18},
        {"id": 2, "username": "liulaoshi", "age": 17},
        {"id": 3, "username": "liulaoshi", "age": 16},
        {"id": 4, "username": "liulaoshi", "age": 15},
    ]
    # 返回前端json数据
    return jsonify(data)


from flask import redirect


# 页面跳转响应
@app.route("/user")
def user():
    # 页面跳转 redirect函数就是response对象的页面跳转的封装
    # Location: http://www.baidu.com
    return redirect("http://www.baidu.com")


@app.route("/red")
def red():
    """站内跳转"""
    return redirect("/user")
    # 使用 http://0.0.0.0:5000/red 测试会调到/user再重定向到百度


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1', debug=True)
