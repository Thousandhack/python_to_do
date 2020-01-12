#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask, request, jsonify
from ext import db
from model import Table_01

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()


@app.route('/table', methods=['POST'])
def table():
    name = request.form.get('name')

    table = Table_01(name)
    print("table ID：", table.id)
    db.session.add(table)
    db.session.commit()

    return jsonify({'id': table.id})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
