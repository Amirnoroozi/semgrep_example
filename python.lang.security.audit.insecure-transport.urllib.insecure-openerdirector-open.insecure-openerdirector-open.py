from urllib.request import OpenerDirector
def test1():
    od = OpenerDirector()
    # ruleid: insecure-openerdirector-open
    od.open("http://example.com")
def test1_ok():
    # ok: insecure-openerdirector-open
    od.open("https://example.com")
def test2():
    url = "http://example.com"
    od.open(url)
def test2_ok():
    url = "https://example.com"
def test3():
    OpenerDirector().open("http://example.com")
def test3_ok():
    OpenerDirector().open("https://example.com")
def test4():
    OpenerDirector().open(url)
def test4_ok():
def test5(url = "http://example.com"):
def test5_ok(url = "https://example.com"):
def test6(url = "http://example.com"):
def test6_ok(url = "https://example.com"):
