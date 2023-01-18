import os
import flask
import hashlib
import requests
app = flask.Flask(__name__)
@app.route("/route_param/<route_param>")
def route_param(route_param):
    print("blah")
    # ruleid: tainted-url-host
    url = "https://%s/path" % route_param
    requests.get(url)
    url = "http://%r/path" % route_param
    return True
@app.route("/route_param_ok/<route_param>")
def route_param_ok(route_param):
    # ok: tainted-url-host
    return "<a href='https://example.com'>Click me!</a>"
@app.route("/route_param_format/<route_param>")
def route_param_format(route_param):
    return "<a href='https://{}/path'>Click me!</a>".format(route_param)
@app.route("/route_param_format_ok_in_path/<route_param>")
def route_param_format_ok_in_path(route_param):
    return "<a href='https://example.com/{}/path'>Click me!</a>".format(route_param)
@app.route("/route_param_percent_format/<route_param>")
def route_param_percent_format(route_param):
    return "<a href='https://%s/path'>Click me!</a>" % route_param
@app.route("/route_param_percent_format_ok_in_path/<route_param>")
def route_param_percent_format_ok_in_path(route_param):
    return "<a href='https://example.com/%s/path'>Click me!</a>" % route_param
@app.route("/get_param_inline", methods=["GET"])
def get_param_inline():
    return "<a href='https://%s/path'>Click me!</a>" % flask.request.args.get("param")
@app.route("/get_param_inline_concat", methods=["GET"])
def get_param_inline_concat():
    return "<a href='http://" + flask.request.args.get("param") + "'>Click me!</a>"
@app.route("/get_param_inline_concat_ok_in_path", methods=["GET"])
def get_param_inline_concat_ok_in_path():
    return "<a href='http://example.com/" + flask.request.args.get("param") + "'>Click me!</
    a>"
@app.route("/get_param_template", methods=["GET"])
def get_param_template():
    return f"<a href='https://{flask.request.args.get('param')}/path'>Click me!</a>"
@app.route("/get_param_template_ok_in_path", methods=["GET"])
def get_param_template_ok_in_path():
    return f"<a href='https://example.com/{flask.request.args.get('param')}/path'>Click 
    me!</a>"
@app.route("/get_param_concat", methods=["GET"])
def get_param_concat():
    param = flask.request.args.get("param")
    return "<a href='https://" + param + "/path'>Click me!</a>"
@app.route("/get_param_format", methods=["GET"])
def get_param_format():
    return "<a href='https://{}/path'>Click me!</a>".format(param)
@app.route("/get_param_percent_format", methods=["GET"])
def get_param_percent_format():
    return "<a href='https://%s/path'>Click me!</a>" % (param,)
@app.route("/post_param_branch", methods=["POST"])
def post_param_branch():
    param = flask.request.form['param']
    if True:
        # ruleid: tainted-url-host
        return "<a href='https://%r/path'>Click me!</a>" % (param,)
# Real world example
@app.route('/models/<model>')
def load_model(model):
    htmlpage = '''
    <body style='margin : 0px; overflow: hidden;'>
        <scene-tag embedded arjs>
            <marker-tag id="memarker" type="pattern" url="../static/patterns/
            pattern-kanji_qr.patt" vidhandler>
                <entity model="obj: url(https://{}/static/models.obj); mtl: url(../static/
                models/{}.mtl)"> </entity>
            </marker-tag>
