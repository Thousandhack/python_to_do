#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask, jsonify
from flask import redirect, url_for

app = Flask(__name__)


@app.route("/my_json")
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


@app.route("/red")
def red():
    """站内跳转"""
    return redirect(url_for("json"))
    # 使用 http://0.0.0.0:5000/red 测试会重定/json 得到json数据


if __name__ == '__main__':
    app.run(port=9001, host='127.0.0.1', debug=True)
