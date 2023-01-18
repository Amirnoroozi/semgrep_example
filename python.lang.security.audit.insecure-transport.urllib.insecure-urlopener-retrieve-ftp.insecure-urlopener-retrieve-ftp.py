from urllib.request import URLopener
def test1():
    od = URLopener()
    # ruleid: insecure-urlopener-retrieve-ftp
    od.retrieve("ftp://example.com")
def test1_ok():
    # ok: insecure-urlopener-retrieve-ftp
    od.retrieve("ftps://example.com")
def test2():
    url = "ftp://example.com"
    od.retrieve(url)
def test2_ok():
    url = "ftps://example.com"
def test3():
    URLopener().retrieve("ftp://example.com")
def test3_ok():
    URLopener().retrieve("ftps://example.com")
def test4():
    URLopener().retrieve(url)
def test4_ok():
def test5(url = "ftp://example.com"):
def test5_ok(url = "ftps://example.com"):
def test6(url = "ftp://example.com"):
def test6_ok(url = "ftps://example.com"):
