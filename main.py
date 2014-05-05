# -*- coding: utf-8 -*-
from bottle import Bottle, run, template, request


app = Bottle()


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/hello')
@app.route('/hello/')
@app.route('/hello/<name:re:[a-z]+>')
def greet(name='stranger'):
    return template('Hello {{name}}, how are you?', name=name)


@app.get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
        Username: <input name="username" type="text" />
        Password: <input name="password" type="password" />
        <input value="Login" type="submit" />
        </form>
        '''


@app.post('/login') # or @app.route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


def check_login(username, password):
    return username == password


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)