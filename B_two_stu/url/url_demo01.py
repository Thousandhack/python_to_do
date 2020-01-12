#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

from flask import Flask

app = Flask(__name__)


# 加载项目配置
# 配置类
class Config(object):
    DEBUG = True


app.config.from_object(Config)


# 路由传递参数[没有限定类型]
@app.route('/user/<user_id>')
def user_info_1(user_id):
    return 'hello info_1 %s' % user_id


# 路由传递参数[限定数据类型],列子是用了int类型,可以选择bool,float都可以的
# user_id 必须是整数
@app.route('/user/<int:user_id>')
def user_info_2(user_id):
    return 'hello info_2 %d' % user_id


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
    """
    测试说明：
        测试1：
        http://127.0.0.1:9000/user/qwer
        这样的情况是访问了函数1的url,因为qwerb不为整数，所以路由到没有限定类型处
        测试2：
        http://127.0.0.1:9000/user/2
        这样的情况下会选择有限定类型的路由
        测试3：
        注释限定的，让后使用如下url测试：
        http://127.0.0.1:9000/user/2
        这样会走无限定的路由
    """
