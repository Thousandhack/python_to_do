#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
# 使用原生的SQL 应用SQLAlchemy
# 首先需要学习一下create_engine
# engine = create_engine('dialect+driver://username:password@host:port/database')
#
# dialect -- 数据库类型
#
# driver -- 数据库驱动选择
#
# username -- 数据库用户名
#
# password -- 用户密码
#
# host 服务器地址
#
# port 端口
#
# database 数据库
from sqlalchemy import create_engine
from consts import DB_URL

engine = create_engine(DB_URL)
conn = engine.connect()

conn.execute('drop table if exists users')
conn.execute('create table users(id int primary key auto_increment,'
             'name varchar(25))')
conn.execute("insert into users(name) values('xiaoming')")
conn.execute("insert into users(name) values('xiaohei')")

rs = conn.execute('select * from users')

for row in rs:
    print(row)

# 关于 create_engine 的用法
# engine = create_engine('dialect+driver://username:password@host:port/database')
#
# dialect -- 数据库类型
#
# driver -- 数据库驱动选择
#
# username -- 数据库用户名
#
# password -- 用户密码
#
# host 服务器地址
#
# port 端口
#
# database 数据库

# 如下介绍几种常用驱动和相应数据库的连接


