#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

# 下面编写一个自定义路由转换器

from flask import Flask

app = Flask(__name__)

# 导入转换器基类
from werkzeug.routing import BaseConverter


class MobileNumberConverter(BaseConverter):
    """
    手机号码的自定义路由转换器
    """
    regex = "\d{11}"


# 添加转换器到默认的转换器字典中，并指定转换器使用时名字为: mobile
app.url_map.converters['mobile'] = MobileNumberConverter


# 使用转换器去实现自定义匹配规则
@app.route(r"/sms/<mobile:mobile_number>/")  # mobile_number就是测试的电话号码
def sms(mobile_number):
    """
    通过以下url访问:
    http://127.0.0.1:9000/sms/13666666666/
    :param mobile_number:
    :return:
    """
    print(mobile_number)
    return "手机号通过,短信"


# 例2
class RegexConverter(BaseConverter):
    """正在路由转换器"""

    def __init__(self, url_map, *args):
        # super().__init__(url_map)  # 或者这样写
        # url_map 所有url组成的元组
        # url_map相当于django中的urlpatterns
        super(RegexConverter, self).__init__(url_map)  # 初始化分类
        self.regex = args[0]  # 是一个元组


app.url_map.converters['reg'] = RegexConverter


# \w 表示大写字母小写字母下划线
@app.route(r"/register/<reg('\w{4,6}'):username>/")
def reg(username):  # 这个函数名没有限制
    """
    通过以下url访问:
    http://127.0.0.1:9000/register/qwer/
    :param username:
    :return:
    """
    print(username)
    return "ok reg"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
