from flask import Flask

app = Flask(__name__)


@app.route('/item/<id>/')
def item(id):
    return 'Item:{}'.format(id)


@app.route('/projects/')
def projects():
    # http://127.0.0.1:5000/projects/
    return 'The project page'


@app.route('/about')
def about():
    # http://127.0.0.1:5000/about
    return 'The about page'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # 使用以下url访问 可以得到打印结果
    # http://127.0.0.1:5000/item/1/

    # 返回结果为：
    # Item:1
