#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
from flask import Flask, jsonify
from flask.views import MethodView

app = Flask(__name__)


class UserAPI(MethodView):
    def get(self):
        return jsonify({
            'username': 'fake',
            'url': 'wwww'
        })

    def post(self):
        return 'UNSUPPORT!'


app.add_url_rule('/user', view_func=UserAPI.as_view('userview'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

    # 访问
    # http://127.0.0.1:5000/user
    # 返回：
    # {
    #   "url": "wwww",
    #   "username": "fake"
    # }
