# cf. https://github.com/PyCQA/bandit/blob/b78c938c0bd03d201932570f5e054261e10c5750/
examples/crypto-md5.py
import hashlib
# ruleid:insecure-hash-algorithm-md5
hashlib.md5(1)
hashlib.md5(1).hexdigest()
abc = str.replace(hashlib.md5("1"), "###")
print(hashlib.md5("1"))
# ok:insecure-hash-algorithm-md5
hashlib.sha256(1)
