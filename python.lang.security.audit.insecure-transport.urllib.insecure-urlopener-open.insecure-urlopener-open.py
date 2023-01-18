from urllib.request import URLopener
def test1():
    od = URLopener()
    # ruleid: insecure-urlopener-open
    od.open("http://example.com")
def test1_ok():
    # ok: insecure-urlopener-open
    od.open("https://example.com")
def test2():
    url = "http://example.com"
    od.open(url)
def test2_ok():
    url = "https://example.com"
def test3():
    URLopener().open("http://example.com")
def test3_ok():
    URLopener().open("https://example.com")
def test4():
    URLopener().open(url)
def test4_ok():
def test5(url = "http://example.com"):
def test5_ok(url = "https://example.com"):
def test6(url = "http://example.com"):
def test6_ok(url = "https://example.com"):
