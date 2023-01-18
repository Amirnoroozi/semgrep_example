from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# ruleid: no-csrf-exempt
@csrf_exempt
def my_view(request):
    return HttpResponse('Hello world')
import django
@django.views.decorators.csrf.csrf_exempt
def my_view2(request):
