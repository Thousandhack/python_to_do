#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, tuple_
from sqlalchemy.sql import select, asc, and_

from consts import DB_URL

eng = create_engine(DB_URL)

meta = MetaData(eng)
students = Table(
    'Students', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50), nullable=False)
)

if students.exists():
    students.drop()

students.create()

