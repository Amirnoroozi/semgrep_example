import requests
def test1():
    # ruleid: request-with-http
    requests.get("http://example.com")
def test1_ok():
    # ok: request-with-http
    requests.get("https://example.com")
def test2():
    url = "http://example.com"
    requests.post(url)
def test2_ok():
    url = "https://example.com"
def test3(url = "http://example.com"):
    requests.delete(url)
def test3_ok(url = "https://example.com"):
def test4(url = "http://example.com"):
    requests.request("HEAD", url, timeout=30)
def test4_ok(url = "https://example.com"):
def test5(url = "http://example.com"):
    requests.Request("HEAD", url, timeout=30)
def test5_ok(url = "https://example.com"):
def test_localhost_ok(url = "http://localhost/blah"):
