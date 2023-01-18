def test1(request):
    forward = request.GET.get('fwd')
    globs = globals()
    # ruleid: dangerous-globals-use
    function = globs.get(forward)
    if function:
        return function(request)
    env = {'fwd': forward}
    return render(request, 'vulnerable/redirects/forward_failed.html', env)
def test2(request):
    function = locals().get(forward)
def test3(request):
    function = test1.__globals__[forward]
def test4(request):
    result = locals()[forward].__dict__['abs'](-12)
def okTest():
    # ok: dangerous-globals-use
    function = locals().get("test3")
def okTest2(data):
    list_of_globals = globals()
    list_of_globals["foobar"].update(data)
def okTest3(data):
    NS = globals()
    NS['_foobar_' + data] = smth(data)
