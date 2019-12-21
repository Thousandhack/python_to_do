#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
from flask import Flask, jsonify
from werkzeug.wrappers import Response

app = Flask(__name__)


class JSONResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            response = jsonify(response)
        return super(JSONResponse, cls).force_type(response, environ)


app.response_class = JSONResponse


@app.route('/')
def hello_world():
    return {'msg': 'Hello world!'}
    # http://127.0.0.1:5000/
    # 返回接口数据


@app.route('/cunstom_headers')
def header():
    """
    返回接口数据
    http://127.0.0.1:5000/cunstom_headers
    :return:
        {
      "header": [
                1,
                2,
                3
                ]
        }
    """
    return {'header': [1, 2, 3]}, 201, [('X-Request-Id', '100')]


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
