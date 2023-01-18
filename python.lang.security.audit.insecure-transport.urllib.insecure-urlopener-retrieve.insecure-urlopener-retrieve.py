from urllib.request import URLopener
def test1():
    od = URLopener()
    # ruleid: insecure-urlopener-retrieve
    od.retrieve("http://example.com")
def test1_ok():
    # ok: insecure-urlopener-retrieve
    od.retrieve("https://example.com")
def test2():
    url = "http://example.com"
    od.retrieve(url)
def test2_ok():
    url = "https://example.com"
def test3():
    URLopener().retrieve("http://example.com")
def test3_ok():
    URLopener().retrieve("https://example.com")
def test4():
    URLopener().retrieve(url)
def test4_ok():
def test5(url = "http://example.com"):
def test5_ok(url = "https://example.com"):
def test6(url = "http://example.com"):
def test6_ok(url = "https://example.com"):
