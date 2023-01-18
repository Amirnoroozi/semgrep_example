import subprocess
import sys
# ok:subprocess-shell-true
subprocess.call("echo 'hello'")
subprocess.call("grep -R {} .".format(sys.argv[1]))
subprocess.call("echo 'hello'", shell=True)
# ruleid:subprocess-shell-true
subprocess.call("grep -R {} .".format(sys.argv[1]), shell=True)
subprocess.call("grep -R {} .".format(sys.argv[1]), shell=True, cwd="/home/user")
subprocess.run("grep -R {} .".format(sys.argv[1]), shell=True)
