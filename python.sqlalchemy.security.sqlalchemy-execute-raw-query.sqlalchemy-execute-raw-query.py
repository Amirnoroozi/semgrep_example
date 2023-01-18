##########################################################################
# Connectionless query
##########################################################################

# String concatenation using + operator
engine = create_engine('postgresql://user@localhost/database')
echo("database connexion: ok")
# ruleid: sqlalchemy-execute-raw-query
engine.execute("INSERT INTO person (name) VALUES ('" + name + "')")
# ruleid: sqlalchemy-execute-raw-query
engine.execute("INSERT INTO p