from textwrap import dedent
def unsafe(request):
    # ruleid: user-eval
    code = request.POST.get('code')
    print("something")
    eval(code)
def unsafe_inline(request):
    eval(request.GET.get('code'))
def unsafe_dict(request):
    eval(request.POST['code'])
def safe(request):
    # ok: user-eval
    code = """
    print('hello')
    """
    eval(dedent(code))
