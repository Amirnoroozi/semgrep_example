# cf. https://github.com/PyCQA/bandit/blob/b1411bfb43795d3ffd268bef17a839dee954c2b1/
examples/ssl-insecure-version.py
import ssl
from pyOpenSSL import SSL
# ruleid:weak-ssl-version
ssl.wrap_socket(ssl_version=ssl.PROTOCOL_SSLv2)
SSL.Context(method=SSL.SSLv2_METHOD)
SSL.Context(method=SSL.SSLv23_METHOD)
# ok:weak-ssl-version
ssl.wrap_socket(ssl_version=ssl.PROTOCOL_TLSv1_2)
some_other_method(ssl_version=ssl.PROTOCOL_SSLv2)
some_other_method(method=SSL.SSLv2_METHOD)
some_other_method(method=SSL.SSLv23_METHOD)
ssl.wrap_socket(ssl_version=ssl.PROTOCOL_SSLv3)
ssl.wrap_socket(ssl_version=ssl.PROTOCOL_TLSv1)
SSL.Context(method=SSL.SSLv3_METHOD)
SSL.Context(method=SSL.TLSv1_METHOD)
some_other_method(ssl_version=ssl.PROTOCOL_SSLv3)
some_other_method(ssl_version=ssl.PROTOCOL_TLSv1)
some_other_method(method=SSL.SSLv3_METHOD)
some_other_method(method=SSL.TLSv1_METHOD)
ssl.wrap_socket()
def open_ssl_socket(version=ssl.PROTOCOL_SSLv2):
    pass
def open_ssl_socket(version=SSL.SSLv2_METHOD):
def open_ssl_socket(version=SSL.SSLv23_METHOD):
def open_ssl_socket(version=SSL.TLSv1_1_METHOD):
