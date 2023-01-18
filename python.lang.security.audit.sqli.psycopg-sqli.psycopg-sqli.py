import psycopg2
def bad1():
    conn = psycopg2.connect("dbname=test user=postgres")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a command: this creates a new table
    query = "SELECT name FROM users WHERE age=" + req.FormValue("age")
    # ruleid: psycopg-sqli
    cur.execute(query)
def bad2():
    sql_query = 'SELECT * FROM {}'.format(user_input)
    cur.execute(sql_query)
def bad3():
    conn = psycopg2.connect(DSN)
    with conn:
        with conn.cursor() as cur:
            sql_query = 'SELECT * FROM %s'%(user_input)
            # ruleid: psycopg-sqli
            cur.execute(sql_query)
def bad4(user_input):
            sql_query = f'SELECT * FROM {user_input}'
def bad5():
    cur.executemany("SELECT name FROM users WHERE age=" + req.FormValue("age"))
def bad6(user_input):
    cur.execute('SELECT * FROM {}'.format(user_input))
def bad7(user_input):
    cur.execute('SELECT * FROM %s'%(user_input))
def bad8(user_input):
    cur.execute(f'SELECT * FROM {user_input}')
def bad9():
    cur.execute(
    "insert into %s values (%%s, %%s)" % ext.quote_ident(table_name),[10, 20])
def ok1(user_input):
    SQL = "INSERT INTO authors (name) VALUES (%s);"
    # ok: psycopg-sqli
    cur.execute(SQL, user_input)
def ok2(user_input):
    query = "SELECT name FROM users WHERE age=" + "3"
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
