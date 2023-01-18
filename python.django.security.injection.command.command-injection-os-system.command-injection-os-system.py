import os
def danger(request):
    # ruleid: command-injection-os-system
    url = request.GET['url']
    os.system('wget ' + url)
def danger2(request):
    image = request.POST['image']
    os.system("./face-recognize %s --N 24" % image)
def danger3(request):
    os.system("nslookup " + url)
def ok(request):
    # ok: command-injection-os-system
    os.system("echo 'hello'")
