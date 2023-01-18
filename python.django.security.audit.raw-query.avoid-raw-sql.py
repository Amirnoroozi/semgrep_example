query = 'SELECT * FROM myapp_person WHERE last_name = %s' % lname
# ruleid: avoid-raw-sql
Person.objects.raw(query)
# only fires on more than 1 argument
# OK
Person.objects.raw()
def RawSQL(foo: str): pass
RawSQL("testing")
from django.db.models.expressions import RawSQL
queryset.annotate(val=RawSQL("select col from sometable where othercol = %s", (someparam,)))
