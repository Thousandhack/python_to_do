#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
# 创建一个表
import MySQLdb
from consts import HOSTNAME, DATABASE, USERNAME, PASSWORD

# 打开数据库连接
db = MySQLdb.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 如果数据表已经存在使用 excute()方法删除表 班级表：class
cursor.execute("DROP TABLE IF EXISTS class")

# 创建数据表SQL语句
sql = """CREATE TABLE class (
         first_name  CHAR(20) NOT NULL,
         last_name  CHAR(20),
         age INT,  
         sex CHAR(1))"""

cursor.execute(sql)

# 关闭数据库连接
db.close()
