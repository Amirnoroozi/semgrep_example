# cf. https://github.com/PyCQA/bandit/blob/b1411bfb43795d3ffd268bef17a839dee954c2b1/
examples/weak_cryptographic_key_sizes.py
import os
from Crypto.PublicKey import RSA as pycrypto_rsa
from Cryptodome.PublicKey import RSA as pycryptodomex_rsa
# ok:insufficient-rsa-key-size
pycrypto_rsa.generate(bits=2048)
pycryptodomex_rsa.generate(bits=2048)
pycrypto_rsa.generate(4096)
pycryptodomex_rsa.generate(4096)
# ruleid:insufficient-rsa-key-size
pycrypto_rsa.generate(bits=1024)
pycryptodomex_rsa.generate(bits=1024)
pycrypto_rsa.generate(512)
pycryptodomex_rsa.generate(512)
pycrypto_rsa.generate(os.getenv("KEY_SIZE"))
pycryptodomex_rsa.generate(os.getenv("KEY_SIZE"))
