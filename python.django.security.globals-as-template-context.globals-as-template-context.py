import base64
import mimetypes
import os
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.template import Template
# adapted from https://github.com/mpirnat/lets-be-bad-guys/blob/
7cbf11014bfc6dc9e199dc0b8a64e4597bc2338f/badguys/vulnerable/views.py#L95
def file_access(request):
    msg = request.GET.get('msg', '')
    # ok: globals-as-template-context
    return render(request, 'vulnerable/injection/file_access.html',
            {'msg': msg})
def bad1(request):
    # ruleid: globals-as-template-context
    response = render(request, 'vulnerable/xss/form.html', globals())
    response.set_cookie(key='monster', value='omnomnomnomnom!')
    return response
def bad2(request, path='default'):
    env = globals()
    return render(request, 'vulnerable/xss/path.html', env)
def bad3(request):
    response = Template.render(request, 'vulnerable/xss/form.html', globals())
def bad4(request, path='default'):
    return Template.render(request, 'vulnerable/xss/path.html', env)
