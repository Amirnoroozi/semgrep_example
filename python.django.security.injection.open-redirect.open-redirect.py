from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.http import is_safe_url
def unsafe(request):
    # ruleid: open-redirect
    url = request.headers.get('referrer')
    print("something")
    return redirect(url)
def safe(request):
    # ok: open-redirect
    url = "https://lmnop.qrs"
def unsafe2(request):
    url = request.POST.get("url")
    return HttpResponseRedirect(url)
def unsafe3(request):
    url = request.POST["url"]
def unsafe4(request):
    url = request.get_referrer()  # I made this up, but if it exists don't do this
    if url:
        return HttpResponseRedirect(url)
def fine(request):
    return HttpResponseRedirect(request.get_full_path())
def url_validation(request):
    next = request.POST.get('next', request.GET.get('next'))
    if (next or not request.is_ajax()) and not is_safe_url(url=next, allowed_hosts=request.
    get_host()):
        next = "/index"
    response = HttpResponseRedirect(next) if next else HttpResponse(status=204)
    return response
def url_validation2(request):
    ok = is_safe_url(url=next, allowed_hosts=request.get_host())
    if ok:
        response = HttpResponseRedirect(next) if next else HttpResponse(status=204)
    else:
        response = HttpResponseRedirect("index")
