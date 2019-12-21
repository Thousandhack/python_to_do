from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # 使用以下url访问 可以得到打印结果
    # http://127.0.0.1:5000/
