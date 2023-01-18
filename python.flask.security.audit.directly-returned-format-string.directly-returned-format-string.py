# -*- coding: utf-8 -*-
import os
import sqlite3
from flask import Flask
from flask import redirect
from flask import request
from flask import session
from jinja2 import Template
app = Flask(__name__)
@app.route("/loginpage")
def render_login_page(thing):
    # ruleid:directly-returned-format-string
    return '''
<p>{}</p>
<form method="POST" style="margin: 60px auto; width: 140px;">
    <p><input name="username" type="text" /></p>
    <p><input name="password" type="password" /></p>
    <p><input value="Login" type="submit" /></p>
</form>
    '''.format(thing)
@app.route("/loginpage2")
def render_login_page2(thing):
<p>%s</p>
    ''' % thing
@app.route("/loginpage3")
def render_login_page3(thing):
    ''' % (thing,)
@app.route("/loginpage4")
def render_login_page4():
    thing = "blah"
    # the string below is now detected as a literal string after constant
    # propagation
    # ok:directly-returned-format-string
    return thing + '''
    '''
@app.route("/loginpage5")
def render_login_page5():
    # same, now ok thx to the constant propagation
    return f'''
{thing}
def render_login_page5(thing):
# cf. https://raw.githubusercontent.com/Deteriorator/Python-Flask-Web-Development/
53be4c48ffbe7d30a1bde5717658f6de81820360/demo/http/app.py
@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
    respones = '<h1>Hello, %s</h1>' % name
    if 'logged_in' in session:
        respones += '[Authenticated]'
    else:
        respones += '[Not Authenticated]'
    # ruleid: directly-returned-format-string
    return respones
@app.route('/hello2')
def hello2():
    respones = '<h1>Hello, {}</h1>'.format(name)
