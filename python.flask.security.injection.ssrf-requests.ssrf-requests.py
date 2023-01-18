import flask
import requests
app = flask.Flask(__name__)
@app.route("/route_param/<route_param>")
def route_param(route_param):
    print("blah")
    # ruleid: ssrf-requests
    return requests.get(route_param)
@app.route("/route_param_ok/<route_param>")
def route_param_ok(route_param):
    # ok: ssrf-requests
    return requests.get("this is safe")
@app.get("/route_param/<route_param>")
def route_param_without_decorator(route_param):
@app.route("/get_param", methods=["GET"])
def get_param():
    param = flask.request.args.get("param")
    requests.post(param, timeout=10)
@app.route("/get_param_ok", methods=["GET"])
def get_param_ok():
    requests.post("this is safe", timeout=10)
@app.route("/get_param_inline_concat", methods=["GET"])
def get_param_inline_concat():
    requests.get(flask.request.args.get("param") + "/id")
@app.route("/get_param_concat", methods=["GET"])
def get_param_concat():
    requests.get(param + "/id")
@app.route("/get_param_format", methods=["GET"])
def get_param_format():
    requests.get("{}.csv".format(param))
@app.route("/get_param_percent_format", methods=["GET"])
def get_param_percent_format():
    requests.get("%s/id" % (param,))
@app.route("/post_param", methods=["POST"])
def post_param():
    param = flask.request.form['param']
    if True:
        # ruleid: ssrf-requests
        requests.get(param)
@app.route("/subexpression", methods=["POST"])
def subexpression():
    param = "{}".format(flask.request.form['param'])
    print("do things")
    requests.post(param, data={"hello", "world"})
@app.route("/ok")
def ok():
    requests.get("https://www.google.com")
