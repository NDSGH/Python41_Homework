from flask import Flask, request, render_template, redirect, make_response
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def start():
    return redirect('/register/')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        user_login = escape(form_data['login'])
        user_password = escape(form_data['password'])
        if user_login and user_password:
            resp = make_response(render_template('login.html'))
            resp.set_cookie('username_cookie', user_login)
            resp.set_cookie('password_cookie', user_password)
            return resp
    return render_template('register.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        user_login = escape(form_data['login'])
        user_password = escape(form_data['password'])
        if user_login and user_password:
            resp = make_response(render_template('user.html', login=user_login))
            c_login = request.cookies.get('username_cookie')
            c_password = request.cookies.get('password_cookie')
            if user_login == c_login and user_password == c_password:
                return resp
            return render_template('login.html')
    return render_template('login.html')


@app.route('/logout/')
def logout():
    return redirect('/login/')


@app.route('/user/')
def user():
    return redirect('/login/')


if __name__ == '__main__':
    app.run(debug=True)
