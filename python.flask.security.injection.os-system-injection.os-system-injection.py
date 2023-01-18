import os
import flask
import hashlib
app = flask.Flask(__name__)
@app.route("/route_param/<route_param>")
def route_param(route_param):
    print("blah")
    # ruleid: os-system-injection
    return os.system(route_param)
@app.route("/route_param_ok/<route_param>")
def route_param_ok(route_param):
    # ok: os-system-injection
    return os.system("ls -la")
@app.route("/route_param_concat/<route_param>")
def route_param_concat(route_param):
    return os.system("echo " + route_param)
@app.route("/route_param_format/<route_param>")
def route_param_format(route_param):
    return os.system("echo {}".format(route_param))
@app.route("/route_param_percent_format/<route_param>")
def route_param_percent_format(route_param):
    return os.system("echo %s" % route_param)
@app.route("/get_param_inline", methods=["GET"])
def get_param_inline():
    os.system(flask.request.args.get("param"))
@app.route("/get_param_inline_concat", methods=["GET"])
def get_param_inline_concat():
    os.system("echo " + flask.request.args.get("param"))
@app.route("/get_param", methods=["GET"])
def get_param():
    param = flask.request.args.get("param")
    os.system(param)
@app.route("/get_param_concat", methods=["GET"])
def get_param_concat():
    os.system("echo " + param)
@app.route("/get_param_format", methods=["GET"])
def get_param_format():
    os.system("echo {}".format(param))
@app.route("/get_param_percent_format", methods=["GET"])
def get_param_percent_format():
    os.system("echo %s" % (param,))
@app.route("/post_param", methods=["POST"])
def post_param():
    param = flask.request.form['param']
@app.route("/post_param_branch", methods=["POST"])
def post_param_branch():
    if True:
        # ruleid: os-system-injection
        os.system(param)
@app.route("/subexpression", methods=["POST"])
def subexpression():
    param = "{}".format(flask.request.form['param'])
    print("do things")
@app.route("/subexpression_concat", methods=["POST"])
def subexpression_concat():
@app.route("/subexpression_format", methods=["POST"])
def subexpression_format():
@app.route("/subexpression_percent_format", methods=["POST"])
def subexpression_percent_format():
    os.system("echo %s" % param)
# Real world example
@app.route('/', methods=['GET', 'POST'])
def index():
