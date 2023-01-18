import socket
# ruleid:avoid-bind-to-all-interfaces
s = socket.socket(doesnt, matter)
s.bind(('0.0.0.0', 1337))
s.bind(('::', 1337))
s.bind(('',))
# ok:avoid-bind-to-all-interfaces
s.bind(('8.8.8.8', 1337))
s.bind(('fe80::34cb:9850:4868:9d2c', 1337))
