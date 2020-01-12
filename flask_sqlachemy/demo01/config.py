#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

HOSTNAME = 'localhost'
HOSTNAME_2 = '127.0.0.1'
DATABASE = 'flask_stu'
USERNAME = 'flask_user'
PORT = 3306
PASSWORD = '123456'
DB_URL = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME_2, PORT, DATABASE)  # +MySQLdb

DEBUG = True
SQLACHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
