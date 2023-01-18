import requests
class FOO(resource):
    method_decorators = decorator()
    # ok:flask-api-method-string-format
    def get(self, somearg):
        createRecord(somearg)
    # ruleid:flask-api-method-string-format
    def get(self, arg1):
        print("foo")
        string = "foo".format(arg1)
        foo = requests.get(string)
        otherFunc("hello world")
    def get2(self,arg2):
        someFn()
        bar = requests.get("foo".format(arg2))
