#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from consts import DB_URL

eng = create_engine(DB_URL)
Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    # 明天再继续吧 2020 1.9

