from urllib.request import urlopen
def test1():
    # ruleid: insecure-urlopen
    urlopen("http://example.com")
def test1_ok():
    # ok: insecure-urlopen
    urlopen("https://example.com")
def test2():
    url = "http://example.com"
    urlopen(url)
def test2_ok():
    url = "https://example.com"
# ruleid: insecure-urlopen
def test3(url = "http://example.com"):
# ok: insecure-urlopen
def test3_ok(url = "https://example.com"):
