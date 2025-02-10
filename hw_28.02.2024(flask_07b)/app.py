from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/query-string', methods=['GET'])
def index():
    if request.query_string:
        qs = request.args.to_dict()
        return render_template('index.html', qs=qs)
    return render_template('index.html', qs=None)


if __name__ == '__main__':
    app.run(debug=True)
