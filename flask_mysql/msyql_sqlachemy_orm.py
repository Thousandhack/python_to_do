#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker

from consts import DB_URL

eng = create_engine(DB_URL)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, Sequence('user_id_seq'),
                primary_key=True, autoincrement=True)
    name = Column(String(50))


Base.metadata.drop_all(bind=eng)  # 删除表
Base.metadata.create_all(bind=eng)

Session = sessionmaker(bind=eng)
session = Session()

session.add_all([User(name=username) for username in ('xiao hua', 'xiaozhu', 'xiao lin')])
session.commit()


def get_result(rs):
    print('_' * 20)
    for user in rs:
        print(user.name)


# sqlachemy 的orm 的查询语句：
rs = session.query(User).all()
get_result(rs)

rs = session.query(User).filter(User.id.in_([2, ]))
get_result(rs)

rs = session.query(User).filter(and_(User.id > 2, User.id < 4))
get_result(rs)

rs = session.query(User).filter(or_(User.id == 2, User.id == 4))
get_result(rs)



rs = session.query(User).filter(User.name.like('%in%'))
get_result(rs)

rs = session.query(User).filter_by(name='xiao hua').first()
get_result([rs])
