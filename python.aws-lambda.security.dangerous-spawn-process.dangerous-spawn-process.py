import os
import shlex
from somewhere import something
def handler(event, context):
    # ok:dangerous-spawn-process
    os.spawnlp(os.P_WAIT, "ls")
    os.spawnlpe(os.P_WAIT, "ls")
    os.spawnv(os.P_WAIT, "/bin/ls")
    os.spawnve(os.P_WAIT, "/bin/ls", ["-a"], os.environ)
    # ruleid:dangerous-spawn-process
    os.spawnlp(os.P_WAIT, event['cmd'])
    os.spawnlpe(os.P_WAIT, event['cmd'])
    os.spawnv(os.P_WAIT, f"foo-{event['cmd']}")
    os.spawnve(os.P_WAIT, event['cmd'], ["-a"], os.environ)
    os.spawnve(os.P_WAIT, "/bin/bash", ["-c", f"ls -la {event['cmd']}"], os.environ)
    os.spawnl(os.P_WAIT, "/bin/bash", "-c", f"ls -la {event['cmd']}")
    os.spawnl(os.P_WAIT, "/bin/bash", "-c", event['cmd'])
