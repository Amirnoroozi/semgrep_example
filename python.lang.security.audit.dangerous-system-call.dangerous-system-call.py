import os
# ok:dangerous-system-call
os.system("ls -al")
os.popen("cat contents.txt")
from somewhere import something
# ruleid:dangerous-system-call
os.system(something())
getattr(os, "system")(something())
dynamic_system_by_static_os = getattr(os, "system")
dynamic_system_by_static_os(something())
__import__("os").system(something())
getattr(__import__("os"), "system")(something())
dynamic_os = __import__("os")
dynamic_os.system(something())
getattr(dynamic_os, "system")(something())
dynamic_system = getattr(dynamic_os, "system")
dynamic_system(something())
os.popen(something())
os.popen2(something())
