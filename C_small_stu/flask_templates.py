#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask, render_template
from flask import make_response

# 调用了 render_template模板
# 将templates的目录创建在这个应用的同级目录下

app = Flask(__name__)


@app.route('/response')
def my_response():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    # return '<h1>This document carries a cookie!</h1>'  # 效果一样
    return response


# 在templates目录下创建网页
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>/')
def user(name):
    return render_template('user.html', name=name)


# 自定义404错误页面 在templates目录下创建网页
# 输入错误的url返回404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# 自定义500 错误页面 在templates目录下创建网页
@app.errorhandler(500)
def page_not_found(DatabaseError):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
