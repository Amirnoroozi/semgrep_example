# ok:hardcoded-password-default-argument
password = "this-is-probably-a-test"
def say_something(something):
    print(something)
say_something(password)
def say_something_else(something_else="something else"):
    print(something_else)
# ruleid:hardcoded-password-default-argument
def whoops(password="this-could-be-bad"):
    print(password)
def ok(password=None):
