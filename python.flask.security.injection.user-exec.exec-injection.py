import flask
app = flask.Flask(__name__)
@app.route("/route_param/<route_param>")
def route_param(route_param):
    print("blah")
    # ruleid: exec-injection
    return exec(route_param)
@app.route("/route_param_ok/<route_param>")
def route_param_ok(route_param):
    # ok: exec-injection
    return exec("this is safe")
@app.route("/get_param", methods=["GET"])
def get_param():
    param = flask.request.args.get("param")
    exec(param)
@app.route("/get_param_ok", methods=["GET"])
def get_param_ok():
    exec("this is safe")
@app.route("/get_param_inline_concat", methods=["GET"])
def get_param_inline_concat():
    exec("import " + flask.request.args.get("param"))
@app.route("/get_param_concat", methods=["GET"])
def get_param_concat():
    exec(param + "+ 'hello'")
@app.route("/get_param_format", methods=["GET"])
def get_param_format():
    exec("import {}".format(param))
@app.route("/get_param_percent_format", methods=["GET"])
def get_param_percent_format():
    exec("import %s" % (param,))
@app.route("/post_param", methods=["POST"])
def post_param():
    param = flask.request.form['param']
    if True:
        # ruleid: exec-injection
        exec(param)
@app.route("/format", methods=["POST"])
def format():
    param = "{}".format(flask.request.form['param'])
    print("do things")
@app.route("/ok")
def ok():
    exec("This is fine")
