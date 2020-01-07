#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
# Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
#
# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall():接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
# 数据库查询操作

import MySQLdb
from consts import HOSTNAME, DATABASE, USERNAME, PASSWORD

# 打开数据库连接
db = MySQLdb.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM class WHERE age > %s" % (19)

try:
    # 指性SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s" % (fname, lname, age, sex))

except:
    print("Error: unable to fecth data")

# 关闭数据库连接
db.close()
