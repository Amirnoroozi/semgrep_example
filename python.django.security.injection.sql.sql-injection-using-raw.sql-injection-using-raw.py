from django.http import HttpResponse
class Person(models.Model):
    first_name = models.CharField(...)
    last_name = models.CharField(...)
    birth_date = models.DateField(...)
##### raw() True Positives #########
def get_user_age(request):
  # ruleid: sql-injection-using-raw
  user_name = request.get('user_name')
  user_age = Person.objects.raw('SELECT user_age FROM myapp_person where user_name = %s' % 
  user_name)
  html = "<html><body>User Age %s.</body></html>" % user_age
  return HttpResponse(html)
  user_age = Person.objects.raw(f"SELECT user_age FROM myapp_person where user_name = 
  {user_name}")
  user_age = Person.objects.raw('SELECT user_age FROM myapp_person where user_name = %s'.
  format(user_name))
def get_users(request):
  client_id = request.headers.get('client_id')
  users = Person.objects.raw('SELECT * FROM myapp_person where client_id = %s' % client_id)
  html = "<html><body>Users %s.</body></html>" % users
  users = Person.objects.raw(f'SELECT * FROM myapp_person where client_id = {client_id}')
##### raw() True Negatives #########
  # django queryset is good
  user_age = Person.objects.filter(user_name=user_name).first()
  # using param list is ok
  users = Person.objects.raw('SELECT * FROM myapp_person where client_id = %s', 
  (client_id,))
