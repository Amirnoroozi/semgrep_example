from ratelimit.decorators import ratelimit
def missing_view(request):
    pass
@csrf_exempt
def other_decorator(request):
@ratelimit(key=’user’, rate=’10/s’)
def my_view(request):
@ratelimit(key='ip', rate='100/h')
def secondview(request):
