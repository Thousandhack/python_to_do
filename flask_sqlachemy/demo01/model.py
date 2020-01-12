#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
from ext import db


class Table_01(db.Model):
    __tablename__ = 'table_01'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, name, email):
        self.name = name
        self.email = email
