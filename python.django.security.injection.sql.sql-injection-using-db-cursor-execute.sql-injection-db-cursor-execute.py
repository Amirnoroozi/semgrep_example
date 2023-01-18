from django.db import connection
##### True Positives #########
def fetch_name_0(request):
  with connection.cursor() as cursor:
      # ruleid: sql-injection-db-cursor-execute
      cursor.execute(f"SELECT foo FROM bar WHERE baz = {request.data.get('baz')}")
      cursor.execute("SELECT foo FROM bar WHERE baz = %s" % request.data.get('baz'))
      cursor.execute("SELECT foo FROM bar WHERE baz = %s".format(request.data.get('baz')))
      row = cursor.fetchone()
  return row
def fetch_name_1(request):
  # ruleid: sql-injection-db-cursor-execute
  baz = request.data.get("baz")
      cursor.execute(f"UPDATE bar SET foo = 1 WHERE baz = {baz}")
      cursor.execute(f"SELECT foo FROM bar WHERE baz = {baz}")
def fetch_name_2(request):
      cursor.execute("SELECT foo FROM bar WHERE baz = %s" % baz)
def fetch_name_3(request):
      cursor.execute("SELECT foo FROM bar WHERE baz = %s".format(baz))
def upload(request, project_id):
    if request.method == 'POST':
        proj = Project.objects.get(pk=project_id)
        form = ProjectFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Dependent on feature in develop
            # todoruleid: sql-injection-db-cursor-execute
            name = request.POST.get('name', False)
            upload_path = store_uploaded_file(name, request.FILES['file'])
            other_name = "{}".format(name)
            curs = connection.cursor()
            curs.execute(
                "insert into taskManager_file ('name','path','project_id') values ('%s',
                '%s',%s)" %
                (other_name, upload_path, project_id))
##### True Negatives #########
def fetch_name_4(request):
  # using param list is ok
      cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [baz])
      cursor.execute("SELECT foo FROM bar WHERE baz = %s", [baz])
