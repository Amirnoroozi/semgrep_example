from urllib.request import urlopen
def test1():
    # ruleid: insecure-urlopen-ftp
    urlopen("ftp://example.com")
def test1_ok():
    # ok: insecure-urlopen-ftp
    urlopen("sftp://example.com")
def test2():
    url = "ftp://example.com"
    urlopen(url)
def test2_ok():
    url = "sftp://example.com"
# ruleid: insecure-urlopen-ftp
def test3(url = "ftp://example.com"):
# ok: insecure-urlopen-ftp
def test3_ok(url = "sftp://example.com"):
