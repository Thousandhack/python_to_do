#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from consts import DB_URL

# 返回数据库引擎实例
eng = create_engine(DB_URL)
# declarative_base是一个类工厂方法，返回一个基类，并绑定Metadata，
# 通过继承这个基类，就可以在python代码中创建实体类，然后映射到数据库表。
Base = declarative_base()


# 创建一个实体类
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    # 明天再继续吧 2020 1.9
    # 于2020.1.11继续


class Address(Base):
    __tablename__ = 'address'
    # 默认就是自增长, 不加autoincrement=True参数也可
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(128), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    # user字段关联User表
    user = relationship('User', back_populates='addresses')


# 这个字段需要放在Address类定义之后
User.addresses = relationship('Address', order_by=Address.id, back_populates='User')

# 删除表与创建表
Base.metadata.drop_all(bind=eng)
Base.metadata.create_all(bind=eng)

# sessionmaker同样是一个类工厂函数，返回一个Session对象，使用前需要手动实例化并绑定数据库连接引擎。
Session = sessionmaker(bind=eng)
session = Session()

user = User(name='lin')

user.addresses = [Address(email_address='123@qq.com', user_id=user.id),
                  Address(email_address='234@qq.com', user_id=user.id)]

session.add(user)
session.commit()

# 以上实例有错
