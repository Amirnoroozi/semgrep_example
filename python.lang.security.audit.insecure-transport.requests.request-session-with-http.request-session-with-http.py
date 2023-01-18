import requests
def test1():
    session = requests.Session()
    # ruleid: request-session-with-http
    session.get("http://example.com")
def test1_ok():
    # ok: request-session-with-http
    session.get("https://example.com")
def test2():
    url = "http://example.com"
    session.post(url)
def test2_ok():
    url = "https://example.com"
def test3(url = "http://example.com"):
    session.delete(url)
def test3_ok(url = "https://example.com"):
def test4(url = "http://example.com"):
    session.request("HEAD", url, timeout=30)
def test4_ok(url = "https://example.com"):
def test_localhost_ok(url = "http://localhost/blah"):
def test_localhost_ok2(url = "http://127.0.0.1/blah"):
