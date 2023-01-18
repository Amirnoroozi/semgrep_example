import os
# ok:dangerous-system-call-tainted-env-args
os.system("ls -al")
os.popen("cat contents.txt")
from somewhere import something
# fn:dangerous-system-call-tainted-env-args
os.system(something())
os.popen(something())
os.popen2(something())
# Environment true positives
def env1():
    envvar1 = os.environ["envvar"]
    # ruleid:dangerous-system-call-tainted-env-args
    os.system(envvar1)
    os.popen(envvar1)
    os.popen2(envvar1)
    envvar2 = os.environ.get("envvar")
    os.system(envvar2)
    os.popen(envvar2)
    os.popen2(envvar2)
    envvar3 = os.getenv("envvar")
    os.system(envvar3)
    os.popen(envvar3)
    os.popen2(envvar3)
# Cmd line args
import argparse
def args1():
    parser = argparse.ArgumentParser(description="Oops!")
    parser.add_argument("arg1", type=str)
    args = parser.parse_args()
    arg1 = args.arg1
    os.system(arg1)
    os.popen(arg1)
    os.popen2(arg1)
import optparse
def args2():
    parser = optparse.OptionParser()
    parser.add_option(
        "-f", "--file", dest="filename", help="write report to FILE", metavar="FILE"
    )
    (opts, args) = parser.parse_args()
    opt1 = opts.opt1
    os.system(opt1)
    os.popen(opt1)
    os.popen2(opt1)
import getopt
import sys
def args3():
    opts, args = getopt.getopt(
        sys.argv[1:],
        "hl:p:",
        ["help", "local_path", "parameter"],
    for opt, arg in opts:
        # ruleid:dangerous-system-call-tainted-env-args
        os.system(arg)
        os.popen(arg)
        os.popen2(arg)
