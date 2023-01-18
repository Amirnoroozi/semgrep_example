from textwrap import dedent
def unsafe(request):
    # ruleid: user-eval-format-string
    message = request.POST.get('message')
    print("do stuff here")
    code = """
    print(%s)
    """ % message
    eval(code)
def unsafe_inline(request):
    eval("print(%s)" % request.GET.get('message'))
def unsafe_dict(request):
    eval("print(%s)" % request.POST['message'])
def safe(request):
    # ok: user-eval-format-string
    print('hello')
    """
    eval(dedent(code))
def fmt_unsafe(request):
    print({})
    """.format(message)
def fmt_unsafe_inline(request):
    eval("print({})".format(request.GET.get('message')))
def fmt_unsafe_dict(request):
    eval("print({}, {})".format(request.POST['message'], "pwned"))
def fmt_safe(request):
def fstr_unsafe(request):
    code = f"""
    print({message})
def fstr_unsafe_inline(request):
    # todoruleid: user-eval-format-string
    eval(f"print({request.GET.get('message')})")
def fstr_unsafe_dict(request):
    eval(f"print({request.POST['message']})")
def fstr_safe(request):
    var = "hello"
    print('{var}')
