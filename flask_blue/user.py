#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/user')

bg = Blueprint('root', __name__, url_prefix='/root')


@bp.route('/')
def index():
    return "User's Index page"


@bp.route('/1')
def one():
    return "User's 1 page"


@bg.route('/')
def RootIndex():
    return "Root's Index page"
