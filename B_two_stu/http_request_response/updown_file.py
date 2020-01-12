#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"
from flask import Flask
from flask import request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route("/file", methods=['post'])
def form():
    UPLOAD_FOLDER = 'static\\uploads'  # 文件下载路径   win10
    # UPLOAD_FOLDER = 'static/Uploads'  # 文件下载路径  linux
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'jpg'])  # 文件允许上传格式
    """接收上传文件"""
    print(request.files)
    """
    postman上传类型：form-data
    一个文件和一个user:zero
    打印：
    ImmutableMultiDict([('user', 'zero')])
    ImmutableMultiDict([('notes', <FileStorage: '笔记.txt' ('text/plain')>)])
    FileStorage是一个对象
    """
    print(request.files.get('notes'))
    """
    可以调用FileStorage里面的save方法进行文件上传的保存到指定的地址
    """
    # 获取当前项目的目录
    # 也就是当前文科的目录
    print(os.path.abspath(os.path.dirname(__file__)))
    current_path = os.path.abspath(os.path.dirname(__file__))
    files = request.files.get('notes')
    if files and ALLOWED_EXTENSIONS:
        from unicodedata import normalize
        filename = secure_filename(normalize('NFKD', files.filename).encode('utf-8', 'ignore').decode('utf-8'))
        # 使用secure_filename()让文件名变得安全
        # \Lib\site-packages\werkzeug\utils.py
        # 这边需要注意中文文件名上传无法获取中文文件名问题
        print(filename)
        # filename = filename.encode('utf-8', 'strict').decode('utf-8')
        print(filename)
        path = os.path.join(current_path, UPLOAD_FOLDER, filename)  # 路径拼接
        print(path)
        files.save(path)

    return "file uploads ok"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
