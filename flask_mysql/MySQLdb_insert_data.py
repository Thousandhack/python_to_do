#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

# 数据库插入数据操作操作
import MySQLdb
from consts import HOSTNAME, DATABASE, USERNAME, PASSWORD

# 打开数据库连接
db = MySQLdb.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句  注意每运行一次就是一次数据的插入
sql = """INSERT INTO class(first_name,
         last_name, age, sex)
         VALUES ('Linux', 'ubuntu', 18, 'M')"""
print(sql)

"""  """
# # SQL 插入语句 这个语句需要注意
# sql = "INSERT INTO class(first_name,last_name, age, sex) " \
#       "VALUES ('%s', '%s', '%s', '%s')" % ('zero','one', 10,'w')

try:
    # 执行sql语句
    print(sql)
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果有错误
    db.rollback()

# 关闭数据库连接
db.close()
