import os
import shlex
from somewhere import something
# ok:dangerous-spawn-process-audit
os.spawnlp(os.P_WAIT, "ls")
os.spawnlpe(os.P_WAIT, "ls")
os.spawnv(os.P_WAIT, "/bin/ls")
os.spawnve(os.P_WAIT, "/bin/ls", ["-a"], os.environ)
# ruleid:dangerous-spawn-process-audit
os.spawnlp(os.P_WAIT, something())
os.spawnlpe(os.P_WAIT, something())
os.spawnv(os.P_WAIT, something())
os.spawnve(os.P_WAIT, something(), ["-a"], os.environ)
os.spawnve(os.P_WAIT, "/bin/bash", ["-c", something()], os.environ)
# ruleid:dangerous-spawn-process-audit 
os.spawnl(os.P_WAIT, "/bin/bash", "-c", something())
def run_payload(shell_command: str) -> None:
    args = shlex.split(shell_command)
    path = args[0]
    # ruleid:dangerous-spawn-process-audit
    pid = os.posix_spawn(path, args, os.environ)
    os.waitpid(pid, 0)
