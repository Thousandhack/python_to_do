#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/people/')
def people():
    # http://127.0.0.1:9000/people/?name=111
    name = request.args.get('name')
    print(name)

    return jsonify({"name": name})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
