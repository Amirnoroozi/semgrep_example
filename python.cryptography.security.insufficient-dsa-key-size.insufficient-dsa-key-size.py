from cryptography.hazmat import backends
from cryptography.hazmat.primitives.asymmetric import dsa
# ok: insufficient-dsa-key-size
dsa.generate_private_key(key_size=2048,
                         backend=backends.default_backend())
dsa.generate_private_key(2048,
# ruleid: insufficient-dsa-key-size
dsa.generate_private_key(key_size=1024,
dsa.generate_private_key(1024,
