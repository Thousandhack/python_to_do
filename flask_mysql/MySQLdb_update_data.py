#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

# 数据库更新操作
# 更新操作用于更新数据表的的数据，以下实例将 class 表中的 SEX 字段为 'M' 的 age 字段递增 1

import MySQLdb
from consts import HOSTNAME, DATABASE, USERNAME, PASSWORD

# 打开数据库连接
db = MySQLdb.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 更新语句
sql = "UPDATE class SET age = age + 1 WHERE sex = '%c'" % ('M')
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()
