import jwt
secret_const = "this-is-secret"
def bad1():
    # ruleid: jwt-python-hardcoded-secret
    encoded = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    return encoded
def bad1b():
    encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
def bad2():
    encoded = jwt.encode({"some": "payload"}, secret_const, algorithm="HS256")
def bad3():
    secret = "secret"
    encoded = jwt.encode({"some": "payload"}, secret, algorithm="HS256")
def ok(secret_key):
    encoded = jwt.encode({"some": "payload"}, secret_key, algorithm="HS256")
