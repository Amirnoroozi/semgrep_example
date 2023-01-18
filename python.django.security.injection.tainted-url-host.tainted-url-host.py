from django.http import HttpResponse
import requests
class Person(models.Model):
    first_name = models.CharField(...)
    last_name = models.CharField(...)
    birth_date = models.DateField(...)
##### True Positives #########
def ex1(request):
  env = request.POST.get('env')
  user_name = request.POST.get('user_name')
  # ruleid: tainted-url-host
  user_age = requests.get("https://%s/%s/age" % (env, user_name))
  return HttpResponse(user_age)
def ex2(request):
  user_age = requests.get("https://{}/{}/age".format(env, user_name))
def ex3(request):
  user_age = requests.get(f"https://{env}/{user_name}/age")
def ex4(request):
  user_age = requests.get(f"https://" + env + "/" + user_name + "/age")
def ex5(request):
  url = "https://{}/{}/age".format(env, user_name)
  user_age = requests.get(url)
def ex6(request):
def ex7(request):
  url = "https://%s/%s/age"
  user_age = requests.get(url % (env, user_name))
def ex8(request):
  url = "https://{}/{}/age"
  user_age = requests.get(url.format(env, user_name))
##### True Negatives #########
def ok1(request):
  # ok: tainted-url-host
  user_age = requests.get("https://example.com/%s/%s/age" % (env, user_name))
def ok2(request):
  user_age = requests.get("https://example.com/%s/%s/age".format(env, user_name))
