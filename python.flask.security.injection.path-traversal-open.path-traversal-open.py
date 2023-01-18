import flask
import json
app = flask.Flask(__name__)
@app.route("/route_param/<route_param>")
def route_param(route_param):
    print("blah")
    # ruleid: path-traversal-open
    return open(route_param, 'r').read()
@app.route("/route_param_ok/<route_param>")
def route_param_ok(route_param):
    # ok: path-traversal-open
    return open("this is safe", 'r').read()
@app.route("/route_param_with/<route_param>")
def route_param_with(route_param):
    with open(route_param, 'r') as fout:
        return fout.read()
@app.route("/route_param_with_ok/<route_param>")
def route_param_with_ok(route_param):
    with open("this is safe", 'r') as fout:
@app.route("/route_param_with_concat/<route_param>")
def route_param_with_concat(route_param):
    with open(route_param + ".csv", 'r') as fout:
@app.route("/get_param", methods=["GET"])
def get_param():
    param = flask.request.args.get("param")
    f = open(param, 'w')
    f.write("hello world")
@app.route("/get_param_inline_concat", methods=["GET"])
def get_param_inline_concat():
    return open("echo " + flask.request.args.get("param"), 'r').read()
@app.route("/get_param_concat", methods=["GET"])
def get_param_concat():
    return open(param + ".csv", 'r').read()
@app.route("/get_param_format", methods=["GET"])
def get_param_format():
    return open("{}.csv".format(param)).read()
@app.route("/get_param_percent_format", methods=["GET"])
def get_param_percent_format():
    return open("echo %s" % (param,), 'r').read()
@app.route("/post_param", methods=["POST"])
def post_param():
    param = flask.request.form['param']
    if True:
        # ruleid: path-traversal-open
        with open(param, 'r') as fin:
            data = json.load(fin)
    return data
def post_param_with_inline():
    with open(flask.request.form['param'], 'r') as fin:
        data = json.load(fin)
def post_param_with_inline_concat():
    with open(flask.request.form['param'] + '.csv', 'r') as fin:
@app.route("/subexpression", methods=["POST"])
def subexpression():
    param = "{}".format(flask.request.form['param'])
    print("do things")
    return open(param, 'r').read()
@app.route("/ok")
def ok():
    open("static/path.txt", 'r')
