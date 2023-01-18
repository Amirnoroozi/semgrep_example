import requests
# ok:no-auth-over-http
good_url = "https://www.github.com"
bad_url = "http://www.github.com"
# ruleid:no-auth-over-http
r = requests.post("http://www.github.com", auth=('user', 'pass'))
r = requests.post(good_url, auth=('user', 'pass'))
r = requests.get(bad_url, timeout=50)
def test1():
    # ruleid:no-auth-over-http
    bad_url = "http://www.github.com"
    print("something")
    r = requests.get(bad_url, auth=('user', 'pass'))
def test2():
    # ok:no-auth-over-http
    r = requests.post(bad_url)
def test3():
    good_url = "https://www.github.com"
    r = requests.get(good_url, auth=('user', 'pass'))
def from_import_test1(url):
    from requests import get, post
    r = get(good_url, timeout=3)
    r = post(bad_url)
    r = get(bad_url, timeout=3, auth=('user', 'pass'))
