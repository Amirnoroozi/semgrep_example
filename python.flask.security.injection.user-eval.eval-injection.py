import flask
app = flask.Flask(__name__)
@app.route("/route_param/<route_param>")
def route_param(route_param):
    print("blah")
    # ruleid: eval-injection
    return eval(route_param)
    # ok: eval-injection
    return eval("this is safe")
@app.route("/get_param", methods=["GET"])
def get_param():
    param = flask.request.args.get("param")
    eval(param)
    eval("this is safe")
@app.route("/get_param_inline_concat", methods=["GET"])
def get_param_inline_concat():
    eval("import " + flask.request.args.get("param"))
@app.route("/get_param_concat", methods=["GET"])
def get_param_concat():
    eval(param + "+ 'hello'")
@app.route("/get_param_format", methods=["GET"])
def get_param_format():
    eval("import {}".format(param))
@app.route("/get_param_percent_format", methods=["GET"])
def get_param_percent_format():
    eval("import %s" % (param,))
@app.route("/post_param", methods=["POST"])
def post_param():
    param = flask.request.form['param']
    if True:
        # ruleid: eval-injection
        eval(param)
@app.route("/format", methods=["POST"])
def format():
    param = "{}".format(flask.request.form['param'])
    print("do things")
@app.route("/ok")
def ok():
    eval("This is fine")
