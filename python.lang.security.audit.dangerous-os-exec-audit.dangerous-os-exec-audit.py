import os
from somewhere import something
# ok:dangerous-os-exec-audit
os.execl("/foo/bar", "/foo/bar")
os.execv("/foo/bar", ["/foo/bar", "-a", "-b"])
cmd = something()
# ruleid:dangerous-os-exec-audit
os.execl(cmd, cmd, '--do-smth')
os.execve("/bin/bash", ["/bin/bash", "-c", something()], os.environ)
os.execl("/bin/bash", "/bin/bash", "-c", something())
