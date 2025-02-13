from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/static-page', methods=['GET'])
def static_page():
    response = 'Привет! Я заголовок первого уровня'
    return render_template('static_page.html', response=response)


@app.route('/dynamic-page/<name>', methods=['GET'])
def dynamic_page(name):
    return render_template('dynamic_page.html', name=escape(name))


@app.errorhandler(404)
def not_found(e):
    return render_template('err.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
