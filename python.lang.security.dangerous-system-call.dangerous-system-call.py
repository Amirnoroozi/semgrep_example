import os
# ok:dangerous-system-call
os.system("ls -al")
os.popen("cat contents.txt")
from somewhere import something
# fn:dangerous-system-call
os.system(something())
os.popen(something())
os.popen2(something())
# Flask true positives
import flask
app = flask.Flask(__name__)
@app.route("/route_param/<route_param>")
def route_param(route_param):
    # ruleid:dangerous-system-call
    os.system("prefix" + route_param + "suffix")
    os.popen("prefix" + route_param + "suffix")
    os.popen2("prefix" + route_param + "suffix")
    getattr(os, "system")("prefix" + route_param + "suffix")
    return "oops!"
# Flask true negatives
def route_param2(route_param):
    # ok:dangerous-system-call
    os.system("static")
    os.popen("static")
    os.popen2("static")
    return "ok!"
# Django true positives
from django.http import HttpResponse
def get_user_age1(request):
    user_data = request.POST.get("user_data")
    os.system("prefix" + user_data + "suffix")
    os.popen("prefix" + user_data + "suffix")
    os.popen2("prefix" + user_data + "suffix")
    return HttpResponse("oops!")
# Django true negatives
def get_user_age2(request):
    return HttpResponse("ok!")
# Django Rest true positives
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(["GET", "POST"])
def my_api(req):
    user_data = req.POST.get("user_data")
    return Response()
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
class MyApi(APIView):
    def get(self, req, format=None):
        user_data = req.POST.get("user_data")
