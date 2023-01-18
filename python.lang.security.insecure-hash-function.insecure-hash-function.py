# cf. https://github.com/PyCQA/bandit/blob/b1411bfb43795d3ffd268bef17a839dee954c2b1/
examples/hashlib_new_insecure_functions.py
import hashlib
# ruleid:insecure-hash-function
hashlib.new('md5')
hashlib.new('md4', 'test')
hashlib.new(name='md5', string='test')
hashlib.new('MD4', string='test')
hashlib.new(string='test', name='MD5')
# ok:insecure-hash-function
hashlib.new('sha256')
hashlib.new('SHA512')
