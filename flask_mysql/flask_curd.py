#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
import MySQLdb
from consts import HOSTNAME, DATABASE, USERNAME, PASSWORD

con = MySQLdb.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)
cursor = con.cursor()
with cursor as cur:
    cur.execute('drop table if exists users')
    print("11111111")
    cur.execute('create table users(Id INT PRIMARY KEY AUTO_INCREMENT,'
                'Name VARCHAR(25))')
    print("222222")
    cur.execute("insert into users(Name) values('xiaoming')")
    cur.execute("insert into users(Name) values('wanglang')")
    cur.execute('select * from users')
    # 获取存储过程的查询结果
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print('共查找出', cur.rowcount, '条数据')
    data = cur.execute('update users set Name=%s where Id=%s', ('ming', 1))
    # cur.commit()
    # print(cur)
    # print("Number of rows updated:", data.rowcount)
    #
    # cur = con.cursor(MySQLdb.cursors.DictCursor)
    # cur.execute('select * from users')
    #
    # rows = cur.fetchall()
    # for row in rows:
    #     print(row['Id'],row['Name'])

# try：
#     cur =
