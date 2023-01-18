from urllib.request import Request
def test1():
    # ruleid: insecure-request-object
    Request("http://example.com")
def test1_ok():
    # ok: insecure-request-object
    Request("https://example.com")
def test2():
    url = "http://example.com"
    Request(url)
def test2_ok():
    url = "https://example.com"
# ruleid: insecure-request-object
def test3(url = "http://example.com"):
# ok: insecure-request-object
def test3_ok(url = "https://example.com"):
