import urllib3 as ur3
import ssl as sss
import socket
import ssl
# from https://docs.python.org/3/library/ssl.html
hostname = 'www.python.org'
context = sss.create_default_context()
with socket.create_connection((hostname, 443)) as sock:
    # ok:disabled-cert-validation
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
    # ruleid:disabled-cert-validation
    with context.wrap_socket(sock, server_hostname=hostname, cert_reqs = ssl.CERT_NONE) as 
    ssock:
from urllib3 import PoolManager
manager = PoolManager(10)
r = manager.request('GET', 'http://google.com/')
# ruleid:disabled-cert-validation
manager = PoolManager(10, cert_reqs = ssl.CERT_OPTIONAL)
proxy = ur3.ProxyManager('http://localhost:3128/', cert_reqs = ssl.CERT_NONE)
pool = ur3.connectionpool.HTTPSConnectionPool(cert_reqs=ssl.CERT_OPTIONAL)
pool = ur3.connection_from_url('someurl', cert_reqs= ssl.CERT_NONE)
pool = ur3.connection_from_url('someurl', cert_reqs='NONE')
# ok:disabled-cert-validation
pool = ur3.connection_from_url('someurl', cert_reqs='CERT NONE')
pool = ur3.connection_from_url('someurl', cert_reqs="NONE")
pool = ur3.connection_from_url('someurl', cert_reqs= 'CERT_REQUIRED')
pool = ur3.proxy_from_url('someurl', cert_reqs= ssl.CERT_NONE)
pool = ur3.proxy_from_url('someurl', cert_reqs= ssl.CERT_REQUIED)
pool = ur3.proxy_from_url('someurl', cert_reqs=None)
