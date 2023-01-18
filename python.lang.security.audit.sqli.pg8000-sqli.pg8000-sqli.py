import pg8000.native as pg
import pg8000.dbapi
def bad1():
    conn = pg.Connection("postgres", password="cpsnow")
    query = "SELECT name FROM users WHERE age=" + req.FormValue("age")
    # ruleid: pg8000-sqli
    conn.run(query)
def bad2():
    db = pg8000.connect(**db_connect)
    self.assertEqual(db.notifies, [])
    cursor = db.cursor()
    sql_query = 'SELECT * FROM {}'.format(user_input)
    cursor.execute(sql_query)
def bad3():
    connection = pg8000.connect(os.environ['DB_USER'], password=os.environ['DB_PASSWORD'], 
    port=os.environ['DB_PORT'], host=os.environ['DB_HOST'])
    sql_query = 'SELECT * FROM %s'%(user_input)
    connection.run(sql_query)
def bad4(user_input):
    conn = pg8000.connect(user='postgres', password='password', database='andromedabot')
    cursor = conn.cursor()
    sql_query = f'SELECT * FROM {user_input}'
def bad5():
    conn.executemany("SELECT name FROM users WHERE age=" + req.FormValue("age"))
def bad6(user_input):
    conn.run('SELECT * FROM {}'.format(user_input))
def bad7(user_input):
    conn.run('SELECT * FROM %s'%(user_input))
def bad8(user_input):
    conn.execute(f'SELECT * FROM {user_input}')
def bad9():
    conn.execute(
    "insert into %s values (%%s, %%s)" % table_name,[10, 20])
def ok1(user_input):
    SQL = "INSERT INTO authors (name) VALUES :userinput;"
    # ok: pg8000-sqli
    conn.execute(SQL, userinput=user_input)
def ok2(user_input):
    query = "SELECT name FROM users WHERE age=" + "3"
    conn.execute(query)
def ok3(user_input):
    query = "SELECT name FROM users WHERE age="
    query += "3"
def ok4(user_input):
    query = 'SELECT * FROM John'.format()
def ok5(user_input):
    query = 'SELECT * FROM John'% ()
def ok6(user_input):
    query = f'SELECT * FROM John'
def ok7(user_input):
    conn.execute("SELECT name FROM users WHERE age=" + "3")
def ok8(user_input):
    conn.execute('SELECT * FROM John'.format())
def ok9(user_input):
    conn.execute('SELECT * FROM John'% ())
def ok10(user_input):
    conn.execute(f'SELECT * FROM John')
