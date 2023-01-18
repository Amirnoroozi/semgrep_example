import os
import sys
from somewhere import something
# ok:dangerous-os-exec-tainted-env-args
os.execl("/foo/bar", "/foo/bar")
os.execv("/foo/bar", ["/foo/bar", "-a", "-b"])
cmd = something()
# fn:dangerous-os-exec-tainted-env-args
os.execl(cmd, cmd, "--do-smth")
os.execve("/bin/bash", ["/bin/bash", "-c", something()], os.environ)
os.execl("/bin/bash", "/bin/bash", "-c", something())
cmd = sys.argv[2]
# ruleid:dangerous-os-exec-tainted-env-args
os.execl("/bin/bash", "/bin/bash", "-c", cmd)
cmd2 = os.environ['BAD']
os.execl("/bin/bash", "/bin/bash", "-c", cmd2)
