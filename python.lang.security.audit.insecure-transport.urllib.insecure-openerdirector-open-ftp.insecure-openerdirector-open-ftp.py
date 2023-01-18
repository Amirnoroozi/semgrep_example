from urllib.request import OpenerDirector
def test1():
    od = OpenerDirector()
    # ruleid: insecure-openerdirector-open-ftp
    od.open("ftp://example.com")
def test1_ok():
    # ok: insecure-openerdirector-open-ftp
    od.open("sftp://example.com")
def test2():
    url = "ftp://example.com"
    od.open(url)
def test2_ok():
    url = "sftp://example.com"
def test3():
    OpenerDirector().open("ftp://example.com")
def test3_ok():
    OpenerDirector().open("sftp://example.com")
def test4():
    OpenerDirector().open(url)
def test4_ok():
def test5(url = "ftp://example.com"):
def test5_ok(url = "sftp://example.com"):
def test6(url = "ftp://example.com"):
def test6_ok(url = "sftp://example.com"):
