import os
# ruleid:insecure-file-permissions
os.chmod("file", 0o777)
os.chmod("file", 511)
os.chmod("file", 0x1ff)
os.chmod("file", 0o776)
os.chmod("file", 0o775)
os.chmod("file", 0o774)
os.chmod("file", 0o767)
os.chmod("file", 0o757)
os.chmod("file", 0o747)
os.chmod("file", 0o654)
os.chmod("file", 0o100777)
os.chmod("file", 0o100775)
os.chmod("file", 0o100774)
os.chmod("file", 0o100767)
os.lchmod("file", 0o747)
os.lchmod("file", 0o100777)
f = open("file", 'w')
os.fchmod(f, 0o654)
os.fchmod(f, 0o100775)
# ok:insecure-file-permissions
os.fchmod(f, 423)
os.fchmod(f, 0x1a1)
import stat
os.chmod("file", stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH)
# Try to inject Semgrep. Perms end up OK.
os.chmod("file", stat.S_IRWXU | print("GOTCHA"))
# Try to inject Semgrep.
os.chmod("file", stat.S_IRWXO | print("GOTCHA"))
def ensure_exec_perms(file_):
    st = os.stat(file_)
    # ruleid:insecure-file-permissions
    os.chmod(file_, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    return file_
def ensure_exec_perms2(file_):
    os.chmod(file_, st.st_mode | 0o111)
os.chmod("file", 0o644)
os.chmod("file", 0o444)
os.chmod("file", stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
os.chmod("file", stat.S_IRWXU)
