#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

# 删除操作
# 删除操作用于删除数据表中的数据，以下实例演示了删除数据表 class 中 age 小于 20 的所有数据

import MySQLdb

from consts import HOSTNAME, DATABASE, USERNAME, PASSWORD

# 打开数据库连接
db = MySQLdb.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)

# 使用curor()方法获取操作游标
cursor = db.cursor()

# SQL删除语句
sql = "DELETE FROM class WHERE age < %s" % (20)  #
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误回滚
    print("发生回滚了")
    db.rollback()

# 关闭连接
db.close()
