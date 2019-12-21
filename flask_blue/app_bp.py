#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask
import user

app = Flask(__name__)

# 这个app 这边可以注册多个模块，这样就可以进行不同模块进程不同路由指定了

app.register_blueprint(user.bp)
app.register_blueprint(user.bg)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
    # http://127.0.0.1:5000/user/
    # 通过user 模块，进行路由不同再访问不同的函数

    # http://127.0.0.1:5000/root/
    # 通过root ，返回root中相应的函数
