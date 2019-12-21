from flask import Flask
from flask import make_response
from flask import render_template

app = Flask(__name__)


@app.route('/test/')
def test():
    return 'The test page'


@app.errorhandler(404)
def not_found(error):
    # resp = make_response(, 404)
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=app.debug)
