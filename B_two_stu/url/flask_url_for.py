#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask, url_for
from flask import redirect

app = Flask(__name__)


#
# @app.route('/xxx')
# def a():
#     return redirect(url_for('index'))  # url_for直接对函数访问


@app.route('/index')  # endpoint是别名
def home():
    """
    url_for是个函数接受视图函数的名字（字符串形式）作为参数，返回视图函数对应的url
    通过url_for home 来获取前端输入的url是什么
    :return:
    """
    v = url_for("home")
    print(v)
    return "index"


@app.route('/index/<int:nid>', endpoint="aaa")  # endpoint是别名
def zzz(nid):
    """
    这边使用了别名，将zzz函数别名为aaa
    所以url_for 对的是aaa
    :param nid:
    :return:
    """
    v = url_for("aaa", nid=nid)
    print(v)
    return "index2"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
