import requests
def test1():
    with requests.Session() as session:
        # ruleid: request-session-http-in-with-context
        session.get("http://example.com")
def test1_ok():
        # ok: request-session-http-in-with-context
        session.get("https://example.com")
def test2():
        url = "http://example.com"
        session.post(url)
def test2_ok():
        url = "https://example.com"
def test3():
    url = "http://example.com"
def test3_ok():
    url = "https://example.com"
def test_localhost_ok():
    url = "http://localhost/blah"
