from django.db.models.expressions import RawSQL
from django.http import HttpResponse
##### RawSQL() True Positives #########
def get_user_age(request):
  # ruleid: sql-injection-using-rawsql
  user_name = request.get('user_name')
  user_age = RawSQL('SELECT user_age FROM myapp_person where user_name = %s' % user_name)
  html = "<html><body>User Age %s.</body></html>" % user_age
  return HttpResponse(html)
  user_age = RawSQL(f'SELECT user_age FROM myapp_person where user_name = {user_name}')
  user_age = RawSQL('SELECT user_age FROM myapp_person where user_name = %s'.format
  (user_name))
def get_users(request):
  client_id = request.headers.get('client_id')
  users = RawSQL('SELECT * FROM myapp_person where client_id = %s'.format(client_id))
  html = "<html><body>Users %s.</body></html>" % users
  users = RawSQL(f'SELECT * FROM myapp_person where client_id = {client_id}')
##### raw() True Negatives #########
  # using param list is ok
  users = RawSQL('SELECT * FROM myapp_person where client_id = %s', (client_id,))
