import os
import flask
import hashlib
import requests
from flask_sqlalchemy import SQLAlchemy
app = flask.Flask(__name__)
engine = SQLAlchemy()
@app.route("/insert/person")
def insert_person():
    name = flask.request.args.get("name")
    lastname = "you don't get to pick >:)"
    # String concatenation using + operator
    # ruleid: tainted-sql-string
    engine.execute("INSERT INTO person (name) VALUES ('" + name + "')")
    engine.execute("INSERT INTO person (firstname, lastname) VALUES ('" + name + "','" + 
    lastname + "')")
    # ok: tainted-sql-string
    engine.execute("INSERT INTO person (name) VALUES ('" + lastname +"')")
    # Format strings with %
    engine.execute("INSERT INTO person (name) VALUES ('%s')" % (name))
    engine.execute("INSERT INTO person (name) VALUES ('%s')" % (flask.request.args.get
    ("name")))
    engine.execute("INSERT INTO person (name) VALUES ('%s')" % (lastname))
    # Format strings with .format
    engine.execute("INSERT INTO person (name) VALUES ('{}')".format(name))
    # Format strings  using fstrings
    engine.execute(f"SELECT FROM person WHERE name='{name}'")
    # Query without concatenation
    engine.execute("INSERT INTO person (name) VALUES ('Frodon Sacquet')")
    # Query using prepared statement with named parameters
    stmt = text("INSERT INTO table (name) VALUES(:name)")
    engine.execute(stmt, name=name)
    # SQL Composition and prepared statement
    query = select(literal_column("users.fullname", String) + ', ' + literal_column
    ("addresses.email_address").label("title")).where(and_(literal_column("users.id") == 
    literal_column("addresses.user_id"), text("users.name BETWEEN 'm' AND 'z'"), text("
    (addresses.email_address LIKE :x OR addresses.email_address LIKE :y)"))).select_from
    (table('users')).select_from(table('addresses'))
    engine.execute(query, {"x":"%@aol.com", "y":name}).fetchall()
@app.route("/insert/person/path")
def insert_person(path):
    name = path
    connection.execute(stmt, name=name)
