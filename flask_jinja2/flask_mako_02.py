#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from mako.template import Template

template = Template('Hello ${name}!')
a  = template.render(name='xiaoming')
print(a)
